# meeting-sense

CIS 4330 003 Final Course Project

## Responsibilities

Front End - @MCQv9

- [ ] 2 App Pages ( Homepage & Wordle)
- [ ] Send recoreded audio to server and visulized response

Back End - @rabernethy

- [x] API / Web Server for app
- [x] Pipeline for audio to text translation
- [x] Readme.md document
- [x] wordle creation
- [x] word checking via dictionary for postprocessing

## Pretrained Model

[Pretrained Model wav2vec](https://arxiv.org/pdf/2006.11477.pdf)

[GitHub_Link](https://github.com/pytorch/fairseq/blob/main/examples/wav2vec/README.md)

![Model_Flow_Chart](https://github.com/rabernethy/meeting-sense/blob/main/wav2vecflow.png)

This model uses a multi layer convolution neural network to encode audio then makes a mask of resulting speech then is fed to a transformer network to build contextualized representations. This allows the model to learn from small amounts of data and still preform with a low WER.

## Used External Libraries & Tools

* [Librosa](https://librosa.org/doc/latest/index.html)
* [PyTorch](https://pytorch.org/)
* [Transformers](https://huggingface.co/transformers/)(Specifically Wav2Vec2ForCTC & Wav2Vec2Tokenizer)
* [Wavfile](https://pypi.org/project/wavefile/)
* [Flask](https://pypi.org/project/Flask/)
* [WordCloud](https://github.com/amueller/word_cloud)
