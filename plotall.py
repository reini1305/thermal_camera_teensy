#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 15:34:12 2018

@author: reini
"""

import numpy as np
from scipy.ndimage import zoom
import matplotlib.pyplot as plt
from glob import glob
import os

try:
    os.makedirs('processed')
except:
    pass    

for filename in glob('*.RAW'):
    print 'Processing ' + filename + '...'
    with open(filename,'rb') as f:
        data = np.reshape(np.fromfile(f,dtype=np.uint16),(8,8))/10
    os.rename(filename,'processed/' + filename)
    plt.imshow(zoom(data,32),cmap='plasma')
    plt.colorbar()
    outfilename = 'processed/' + os.path.splitext(filename)[0] + '.png'
    plt.savefig(outfilename, bbox_inches='tight')
    plt.close()
