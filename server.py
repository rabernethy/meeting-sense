# server.py written by Russell Abernethy
# For Smart Sensors Class @ Temple University

import librosa, torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2CTCTokenizer
from flask import Flask, request, jsonify, render_template

filename = './current_audio.wav'

app = Flask(__name__)

@app.route('/asr',methods=['POST'])
def asr():
    audio = request.files['file']
    audio.save( filename )

    audio, rate = librosa.load(filename,sr = 16000)
    input_values = tokenizer(audio, return_tensors = "pt").input_values
    logits = model(input_values).logits
    prediction = torch.argmax(logits, dim = -1)

    return jsonify(tokenizer.batch_decode(prediction)[0])

if __name__ == "__main__":

    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    tokenizer = Wav2Vec2CTCTokenizer.from_pretrained("facebook/wav2vec2-base-960h")

    app.run(debug=True)

