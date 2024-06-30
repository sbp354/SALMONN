# Copyright (2024) Tsinghua University, Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import time

import torch
from torch.utils.data import DataLoader, DistributedSampler
import soundfile as sf
import numpy as np

from SALMONN.dist_utils import is_main_process, get_world_size, get_rank


def now():
    from datetime import datetime

    return datetime.now().strftime("%Y%m%d%H%M")


def setup_logger():
    logging.basicConfig(
        level=logging.INFO if is_main_process() else logging.WARN,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()],
    )


def get_dataloader(dataset, config, is_train=True, use_distributed=True):
    if use_distributed:
        sampler = DistributedSampler(
            dataset,
            shuffle=is_train,
            num_replicas=get_world_size(),
            rank=get_rank()
        )
    else:
        sampler = None

    loader = DataLoader(
        dataset,
        batch_size=config.batch_size_train if is_train else config.batch_size_eval,
        num_workers=config.num_workers,
        pin_memory=True,
        sampler=sampler,
        shuffle=sampler is None and is_train,
        collate_fn=dataset.collater,
        drop_last=is_train,
    )

    if is_train:
        loader = IterLoader(loader, use_distributed=use_distributed)

    return loader


def apply_to_sample(f, sample):
    if len(sample) == 0:
        return {}

    def _apply(x):
        if torch.is_tensor(x):
            return f(x)
        elif isinstance(x, dict):
            return {key: _apply(value) for key, value in x.items()}
        elif isinstance(x, list):
            return [_apply(x) for x in x]
        else:
            return x

    return _apply(sample)


def move_to_cuda(sample):
    def _move_to_cuda(tensor):
        return tensor.cuda()

    return apply_to_sample(_move_to_cuda, sample)


def prepare_sample(samples, cuda_enabled=True):
    if cuda_enabled:
        samples = move_to_cuda(samples)

    # TODO fp16 support

    return samples


class IterLoader:
    """
    A wrapper to convert DataLoader as an infinite iterator.

    Modified from:
        https://github.com/open-mmlab/mmcv/blob/master/mmcv/runner/iter_based_runner.py
    """

    def __init__(self, dataloader: DataLoader, use_distributed: bool = False):
        self._dataloader = dataloader
        self.iter_loader = iter(self._dataloader)
        self._use_distributed = use_distributed
        self._epoch = 0

    @property
    def epoch(self) -> int:
        return self._epoch

    def __next__(self):
        try:
            data = next(self.iter_loader)
        except StopIteration:
            self._epoch += 1
            if hasattr(self._dataloader.sampler, "set_epoch") and self._use_distributed:
                self._dataloader.sampler.set_epoch(self._epoch)
            time.sleep(2)  # Prevent possible deadlock during epoch transition
            self.iter_loader = iter(self._dataloader)
            data = next(self.iter_loader)

        return data

    def __iter__(self):
        return self

    def __len__(self):
        return len(self._dataloader)


def prepare_one_audio_input(wav_path, wav_processor, cuda_enabled=True):
    audio, sr = sf.read(wav_path)
    if len(audio.shape) == 2: # stereo to mono
        audio = audio[:, 0]
    if len(audio) < sr: # pad audio to at least 1s
        sil = np.zeros(sr - len(audio), dtype=float)
        audio = np.concatenate((audio, sil), axis=0)
    audio = audio[: sr * 30] # truncate audio to at most 30s

    # Ensure the spectrogram is properly padded
    spectrogram = wav_processor(audio, sampling_rate=sr, return_tensors="pt", padding='max_length')["input_features"]

    samples = {
        "spectrogram": spectrogram,
        "raw_wav": torch.from_numpy(audio).unsqueeze(0),
        "padding_mask": torch.zeros(len(audio), dtype=torch.bool).unsqueeze(0),
    }
    if cuda_enabled:
        samples = move_to_cuda(samples)

    return samples

def prepare_batch_audio_input(wav_paths, wav_processor):
    batch_samples = {
        "spectrograms": [],
        "raw_wavs": [],
        "padding_masks": [],
    }

    max_spectrogram_length = 0
    max_raw_wav_length = 0
    for wav_path in wav_paths:
        samples = prepare_one_audio_input(wav_path, wav_processor, cuda_enabled=False)
        batch_samples["spectrograms"].append(samples["spectrogram"])
        batch_samples["raw_wavs"].append(samples["raw_wav"])
        batch_samples["padding_masks"].append(samples["padding_mask"])
        max_spectrogram_length = max(max_spectrogram_length, samples["spectrogram"].size(1))
        max_raw_wav_length = max(max_raw_wav_length, samples["raw_wav"].size(1))

    # Pad all spectrograms to the same length
    for i in range(len(batch_samples["spectrograms"])):
        spectrogram_length = batch_samples["spectrograms"][i].size(1)
        if spectrogram_length < max_spectrogram_length:
            padding = torch.zeros((batch_samples["spectrograms"][i].size(0), max_spectrogram_length - spectrogram_length, batch_samples["spectrograms"][i].size(2)))
            batch_samples["spectrograms"][i] = torch.cat([batch_samples["spectrograms"][i], padding], dim=1)

    # Pad all raw waveforms to the same length
    for i in range(len(batch_samples["raw_wavs"])):
        raw_wav_length = batch_samples["raw_wavs"][i].size(1)
        if raw_wav_length < max_raw_wav_length:
            padding = torch.zeros((1, max_raw_wav_length - raw_wav_length))
            batch_samples["raw_wavs"][i] = torch.cat([batch_samples["raw_wavs"][i], padding], dim=1)

    batch_samples["spectrograms"] = torch.cat(batch_samples["spectrograms"], dim=0)
    batch_samples["raw_wavs"] = torch.cat(batch_samples["raw_wavs"], dim=0)
    batch_samples["padding_masks"] = torch.cat(batch_samples["padding_masks"], dim=0)

    return batch_samples

def prepare_text_input(prompts, model_config):
    prompt = [
        model_config.prompt_template.format("<Speech><SpeechHere></Speech> " + prompt.strip()) for prompt in prompts
    ]
    return prompt




