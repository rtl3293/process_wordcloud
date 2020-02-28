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
    ricky_mask = np.array(Image.open("rtrs.jpg"))
    dict = get_rosters(["13", "14", "15", "16", "17", "18", "19"])
    wc = WordCloud(mask=ricky_mask, width=1400, height=1400, contour_width=1, contour_color="white")
    # generate word cloud
    wc.generate_from_frequencies(dict)

    # show
 #   plt.imshow(wc, interpolation="bilinear")
 #   plt.axis("off")
 #   plt.show()
    image = wc.to_file("white_wc.png")
    #image.show()


makeImage()
