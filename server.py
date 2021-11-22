from flask import Flask, request, jsonify, render_template
#from speech_to_text import speech_to_text

app = Flask(__name__)

@app.route('/asr',methods=['POST'])
def asr():
    audio = request.files['file']
    audio.save('./current_audio.wav')

if __name__ == "__main__":

    #model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
    #tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
    app.run(debug=True)

