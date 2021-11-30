"""
Create a wordcloud from a single Python source file
"""

import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS

import numpy as npy
from PIL import Image

dataset = open("test.txt", "r").read()

def create_word_cloud(string):

   maskarray = npy.array(Image.open("cloud.png"))

   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskarray, stopwords = set(STOPWORDS))
   cloud.generate(string)
   cloud.to_file("wordCloud.png")

dataset = dataset.lower()
create_word_cloud(dataset)