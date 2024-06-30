train_prompts = {
    "asr": [
        "<Speech><SpeechHere></Speech> Can you transcribe the speech into a written format?",
        "<Speech><SpeechHere></Speech> Listen to the speech and write down its content.",
        "<Speech><SpeechHere></Speech> What is the content of the speech you heard?",
        "<Speech><SpeechHere></Speech> Please write down the transcription of the speech.",
        "<Speech><SpeechHere></Speech> Please transcribe the speech into a written format.",
        "<Speech><SpeechHere></Speech> Write down the content of the speech you heard.",
        "<Speech><SpeechHere></Speech> Can you write down the transcription of the speech?",
        "<Speech><SpeechHere></Speech> Put the speech into a written format.",
        "<Speech><SpeechHere></Speech> Please help me to transcribe the speech into a written format.",
        "<Speech><SpeechHere></Speech> Recognize the content of the speech you heard.",
        "<Speech><SpeechHere></Speech> Can you recognize what you heard in the speech?",
        "<Speech><SpeechHere></Speech> Recognize the speech and write it down in a written format.",
        "<Speech><SpeechHere></Speech> Listen to the speech and recognize its content.",
        "<Speech><SpeechHere></Speech> Give me the transcription of the speech you heard.",
        "<Speech><SpeechHere></Speech> Recognize the speech and give me the transcription."
    ],
    "asr_zh": [
        "<Speech><SpeechHere></Speech> 前面的语音说了什么？",
        "<Speech><SpeechHere></Speech> 请将语音中的内容写下来。",
        "<Speech><SpeechHere></Speech> 请识别这段中文语音。",
        "<Speech><SpeechHere></Speech> 听前面的音频，写出对方说的内容。",
        "<Speech><SpeechHere></Speech> 写下你听到的内容。",
        "<Speech><SpeechHere></Speech> 请记下语音中人说的话。",
        "<Speech><SpeechHere></Speech> 仔细听这段语音，记下语音中的话",
        "<Speech><SpeechHere></Speech> 将你听到的话写下来",
        "<Speech><SpeechHere></Speech> 这个人说了什么？请记下来。",
        "<Speech><SpeechHere></Speech> 请将语音转换为文字",
        "<Speech><SpeechHere></Speech> 请识别这个人说的内容"
    ],
    "asr_de": [
        "<Speech><SpeechHere></Speech> Können Sie die Rede in ein schriftliches Format übertragen?",
        "<Speech><SpeechHere></Speech> Hören Sie sich die Rede an und schreiben Sie ihren Inhalt auf.",
        "<Speech><SpeechHere></Speech> Bitte notieren Sie die Transkription der Rede.",
        "<Speech><SpeechHere></Speech> Geben Sie mir die Transkription der Rede, die Sie gehört haben.",
        "<Speech><SpeechHere></Speech> Was hat dieser Mann gesagt? Bitte schreiben Sie es auf.",
        "<Speech><SpeechHere></Speech> Können Sie die Transkription der Rede aufschreiben?",
        "<Speech><SpeechHere></Speech> Hören Sie der Stimme aufmerksam zu und notieren Sie die Wörter in der Stimme",
        "<Speech><SpeechHere></Speech> Schreiben Sie auf, was Sie hören.",
        "<Speech><SpeechHere></Speech> Bitte Sprache in Text umwandeln.",
        "<Speech><SpeechHere></Speech> Erkennen Sie den Inhalt der Rede, die Sie gehört haben."
    ],
    "translation_ec": [
        "<Speech><SpeechHere></Speech> Can you translate the speech into Chinese?",
        "<Speech><SpeechHere></Speech> Please translate the speech you heard into Chinese.",
        "<Speech><SpeechHere></Speech> Listen to the speech and translate it into Chinese.",
        "<Speech><SpeechHere></Speech> Give me the Chinese translation of this speech.",
        "<Speech><SpeechHere></Speech> Could you please provide a Chinese translation for the speech?",
        "<Speech><SpeechHere></Speech> Would you be willing to translate the speech into Chinese for me?",
        "<Speech><SpeechHere></Speech> Would you be able to render the speech in Chinese?",
        "<Speech><SpeechHere></Speech> Could you assist me in translating the speech into Chinese?",
        "<Speech><SpeechHere></Speech> Can you help me convert the speech into Chinese text?",
        "<Speech><SpeechHere></Speech> Please convert the speech into Chinese text.",
        "<Speech><SpeechHere></Speech> 请将这段语音的内容翻译成中文。",
        "<Speech><SpeechHere></Speech> 你能把这段语音用中文表达出来吗？",
        "<Speech><SpeechHere></Speech> 请将你听到的语音用中文写出来。"
    ],
    "audiocaption": [
        "<Speech><SpeechHere></Speech> Listen to this audio clip and provide its caption.",
        "<Speech><SpeechHere></Speech> Describe the following audio in a caption.",
        "<Speech><SpeechHere></Speech> Based on the sound you hear, create a caption for this audio.",
        "<Speech><SpeechHere></Speech> Can you describe the scene or event depicted in this audio?",
        "<Speech><SpeechHere></Speech> Could you summarise what's happening in this audio?",
        "<Speech><SpeechHere></Speech> What does this audio describe?",
        "<Speech><SpeechHere></Speech> Please describe the audio."
    ],
    "audiocaption_v2": [
        "<Speech><SpeechHere></Speech> Please write down what your hear in the audio."
    ],
    "QA": [
        "<Speech><SpeechHere></Speech> {}"
    ],
    "inference_QA": [
        "<Speech><SpeechHere></Speech> {}"
    ],
    "gender_QA": [
        "<Speech><SpeechHere></Speech> {}"
    ],
    "gender_recognition": [
        "<Speech><SpeechHere></Speech> What is the gender of the speaker?",
        "<Speech><SpeechHere></Speech> Use one word to describe the speaker's gender.",
        "<Speech><SpeechHere></Speech> Describe the speaker's gender.",
        "<Speech><SpeechHere></Speech> Can you accurately identify the gender of the speaker?",
        "<Speech><SpeechHere></Speech> Can you distinguish the gender of the speaker?",
        "<Speech><SpeechHere></Speech> Describe the gender of the person speaking.",
        "<Speech><SpeechHere></Speech> What is the speaker's gender based on the audio?",
        "<Speech><SpeechHere></Speech> Tell me about the gender of the person you hear.",
        "<Speech><SpeechHere></Speech> Is the speaker male or female?"
    ],
    "phone_recognition": [
        "<Speech><SpeechHere></Speech> Please transcribe the audio clip into its corresponding phonetic representation.",
        "<Speech><SpeechHere></Speech> Write the sequence of phonemes corresponding to this speech.",
        "<Speech><SpeechHere></Speech> Provide the phonetic transcription for the speech.",
        "<Speech><SpeechHere></Speech> Transcribe the phonemes for the speech please.",
        "<Speech><SpeechHere></Speech> Can you recognize the phonetic representation in the speech?",
        "<Speech><SpeechHere></Speech> Listen to the speech and recognize its phonetic representation",
        "<Speech><SpeechHere></Speech> What is the phoneme transcription of the speech?"
    ],
    "speech_separation": [
        "<Speech><SpeechHere></Speech> There are two people talking in the audio, please write what they say in order.",
        "<Speech><SpeechHere></Speech> Please write down what you hear each person says.",
        "<Speech><SpeechHere></Speech> Can you record what each person says?",
        "<Speech><SpeechHere></Speech> Transcribe the words spoken by each person in the audio."
    ],
    "emotion_recognition": [
        "<Speech><SpeechHere></Speech> Describe the emotion of the speaker in one word.",
        "<Speech><SpeechHere></Speech> Use one word to describe the speaker's emotion."
    ],
    "music_description": [
        "<Speech><SpeechHere></Speech> Listen to this music clip and describe the music.",
        "<Speech><SpeechHere></Speech> Please describe the music.",
        "<Speech><SpeechHere></Speech> Provide a description of the music.",
        "<Speech><SpeechHere></Speech> Analyze the music in this clip and offer a description.",
        "<Speech><SpeechHere></Speech> Give me a description of the music in this clip."
    ],
    "speaker_verification": [
        "<Speech><SpeechHere></Speech> Are the two people speaking successively the same person? Answer yes or no.",
        "<Speech><SpeechHere></Speech> Do you only hear the same person talking? Answer yes or no.",
        "<Speech><SpeechHere></Speech> Is only one person speaking in the audio? Answer yes or no."
    ],
    "audio_story_telling": [
        "<Speech><SpeechHere></Speech> Based on the audio, write a story in detail. Your story should be highly related to the audio.",
        "<Speech><SpeechHere></Speech> Please write a story in detail based on the audio. Your story should contain all the elements in the audio.",
        "<Speech><SpeechHere></Speech> Please generate a long story that is highly related to the audio."
    ],
    "speaker_diarization_asr": [
        "<Speech><SpeechHere></Speech> Identify each speaker in turn and what is said.",
        "<Speech><SpeechHere></Speech> Write down the content of each speaker and the corresponding speech in turn.",
        "<Speech><SpeechHere></Speech> Please recognize each speaker and transcribe their speech content."
    ]
}


test_prompts = {
    "asr": "<Speech><SpeechHere></Speech> Recognize the speech and give me the transcription.",
    "asr_zh": "<Speech><SpeechHere></Speech> 请将语音中的内容写下来。",
    "asr_de": "<Speech><SpeechHere></Speech> Hören Sie sich die Rede an und schreiben Sie ihren Inhalt auf.",
    "translation_ec": "<Speech><SpeechHere></Speech> Listen to the speech and translate it into Chinese.",
    "audiocaption": "<Speech><SpeechHere></Speech> Please describe the audio.",
    "audiocaption_v2": "<Speech><SpeechHere></Speech> Please write down what your hear in the audio.",
    "QA": "<Speech><SpeechHere></Speech> {}",
    "gender_QA": "<Speech><SpeechHere></Speech> {}",
    "phone_recognition": "<Speech><SpeechHere></Speech> Provide the phonetic transcription for the speech.",
    "speech_query": "<Speech><SpeechHere></Speech> Please answer the question in detail.",
    "emotion_recognition": "<Speech><SpeechHere></Speech> Describe the emotion of the speaker in one word.", 
    "lyrics_recognition": "<Speech><SpeechHere></Speech> Listen to the song and write down its content.",
    "audio_speech_description": "<Speech><SpeechHere></Speech> Describe the speech and the background audio",
    "speaker_verification": "<Speech><SpeechHere></Speech> Do you only hear the same person talking? Answer yes or no.",
    "fluent_speech_audio": "<Speech><SpeechHere></Speech> Describe the background audio and the speech in a fluent sentence.",
    "speech_separation": "<Speech><SpeechHere></Speech> Please write down what you hear each person says.",
    "audio_story_telling": "<Speech><SpeechHere></Speech> Based on the audio, write a story in detail. Your story should be highly related to the audio.",
    "speech_audio_query": "<Speech><SpeechHere></Speech> Please answer the speaker's question in detail based on the background sound.",
    "slot_filling": "<Speech><SpeechHere></Speech> According to the speech, what is the {}?",
    "music_description": "<Speech><SpeechHere></Speech> Listen to this music clip and describe the music.",
    "translation_en2ja": "<Speech><SpeechHere></Speech> Listen to the speech and translate it into Japanese.",
    "translation_en2de": "<Speech><SpeechHere></Speech> Listen to the speech and translate it into German.",
    "speech_audio_coreasoning": "<Speech><SpeechHere></Speech> Use your strong reasoning skills to answer the speaker's question in detail based on the background sound.",
    "keywords": "<Speech><SpeechHere></Speech> Give me only three keywords of the text.",
    "speaker_diarization_asr": "<Speech><SpeechHere></Speech> Please recognize each speaker and transcribe their speech content."
} 