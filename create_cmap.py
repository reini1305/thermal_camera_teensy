#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:47:15 2018

@author: reini
"""

from __future__ import print_function
from matplotlib import cm
import numpy as np


def rgb_hex565(red, green, blue):
    # take in the red, green and blue values (0-255) as 8 bit values and then combine
    # and shift them to make them a 16 bit hex value in 565 format. 
    print ("0x%0.4X," % ((int(red * 31) << 11) | (int(green * 63) << 5) | (int(blue * 31))),end='')

rgb = cm.plasma(np.arange(256))
for i in np.arange(rgb.shape[0]):
    rgb_hex565(rgb[i][0],rgb[i][1],rgb[i][2])