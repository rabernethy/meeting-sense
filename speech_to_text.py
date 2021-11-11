# toText.py written by Russell Abernethy

import librosa, torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
from sys import argv

filename = argv[1]

# Preprocessing

audio, rate = librosa.load(filename,sr = 16000)
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

input_values = tokenizer(audio, return_tensors = "pt").input_values
logits = model(input_values).logits
prediction = torch.argmax(logits, dim = -1)
transcription = tokenizer.batch_decode(prediction)[0]

print(transcription)