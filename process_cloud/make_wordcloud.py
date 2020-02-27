#!/usr/bin/env python3

import numpy as np

import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
#import matplotlib.pyplot as plt
from get_rosters import get_rosters

def makeImage():
    #ricky_mask = np.array(Image.open("alice_mask.png"))
    dict = get_rosters([2013, 2014, 2015, 2016])
    wc = WordCloud()
    # generate word cloud
    wc.generate_from_frequencies(dict)

    # show
 #   plt.imshow(wc, interpolation="bilinear")
 #   plt.axis("off")
 #   plt.show()
    image = wc.to_file("pic.png")
    #image.show()


makeImage()
