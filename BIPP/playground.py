# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 17:32:29 2018

@author: EPLab
"""

import os
import cv2
import numpy as np
import sys
import time
import imutils
from skimage import measure
import csv

IMAGE_NAME = "channel (2).jpg"
PATH_TO_IMAGE = 'C:/Users/EPLab/Desktop/COCO/BIPP/channels/Dark/'+IMAGE_NAME

image = cv2.imread(PATH_TO_IMAGE)
cv2.imshow("image", imutils.resize(image, width= 100))


height, width, channels = image.shape
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)

# threshold the image to reveal light regions in the
# blurred image
#thresh = cv2.threshold(blurred, 100, 200, cv2.THRESH_BINARY)[1]

## GOOD if luminance > 100
## thresh = cv2.threshold(gray, 170, 255, cv2.THRESH_BINARY)[1]


thresh = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)[1]

# perform a series of erosions and dilations to remove
# any small blobs of noise from the thresholded image#
#thresh = cv2.erode(thresh, None, iterations=1)
#thresh = cv2.dilate(thresh, None, iterations=1)
    
cv2.imshow("image3", imutils.resize(thresh, width= 100))

WhitePixels = cv2.countNonZero(thresh)
BlackPixels = thresh.size - WhitePixels

cv2.waitKey(0)
