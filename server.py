# server.py written by Russell Abernethy
# For Smart Sensors Class @ Temple University

import librosa, torch, wavfile
import noisereduce as nr
from transformers import Wav2Vec2ForCTC, Wav2Vec2CTCTokenizer
from flask import Flask, request, jsonify, render_template




app = Flask(__name__)



@app.route('/asr',methods=['POST'])
def asr():
    filename = './current_audio.wav'
# SENSOR DATA EXTRACTION

    # Data is sent from an andriod tablet running the app & will collected from microphones on the tablet.

    # Load the audio from the received request and save a temporary copy.
    audio = request.files['file']  
    audio.save( filename )

# PREPROCESSING

    # Remove background noise that is irrelevant to the meeting that is being transcibed.
    rate, data = wavfile.read( filename )
    data = nr.reduce_noise(y=data, sr = 16000)
        # Noise Reduction Algorithm Workings:
        # Calculate a spectrogram of the audio clip
        # Calculate a threshold based on the statistic likelyhood of the noises in the audio file
        # Calculate a spectrogram over the signal previousely generated
        # Create a mask that is the difference between the threshold and the spectrogram.
        # The mask is smoothed using a filter that is applied in the time frequency domain
        # The mask is applied to the spectrogram of the signal and is inverted.
    data.save( filename )

# FEATURE EXTRACTION & CLASSIFICATION

    # load the audio file into audio, making sure to sample it at 16000 Hertz
    audio, rate = librosa.load(filename,sr = 16000)

    # tokenize the audio data so that it can be used in the model
    input_values = tokenizer(audio, return_tensors = "pt").input_values

    # store non-normalized predictions based on the logit function applied to the input values
    logits = model(input_values).logits

    # calculate the predicted transcription of the audio file.
    prediction = torch.argmax(logits, dim = -1)

    # return a json object that containing the predicted transcription of the audio
    return jsonify(tokenizer.batch_decode(prediction)[0])

if __name__ == "__main__":

# INITILIZATION OF MODEL & SERVER

    model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    tokenizer = Wav2Vec2CTCTokenizer.from_pretrained("facebook/wav2vec2-base-960h")

    app.run(debug=True)

