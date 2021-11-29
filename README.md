# meeting-sense

CIS 4330 003 Final Course Project

## Pretrained Model

[Pretrained Model wav2vec](https://arxiv.org/pdf/2006.11477.pdf)

![Model_Flow_Chart](https://github.com/rabernethy/meeting-sense/blob/main/wav2vecflow.png)

This model uses a multi layer convolution neural network to encode audio then makes a mask of resulting speech then is fed to a transformer network to build contextualized representations. This allows the model to learn from small amounts of data and still preform with a low WER.

## Used External Libraries & Tools

* [Librosa](https://librosa.org/doc/latest/index.html)
* [PyTorch](https://pytorch.org/)
* [Transformers]()(Specifically Wav2Vec2ForCTC & Wav2Vec2Tokenizer)
* [Wavfile](https://pypi.org/project/wavefile/)
* [Flask](https://pypi.org/project/Flask/)
