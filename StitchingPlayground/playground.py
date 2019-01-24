# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 17:00:01 2019

@author: EPLab
"""

# USAGE
# python stitch.py --first images/bryce_left_01.png --second images/bryce_right_01.png 

# import the necessary packages
from panorama import Stitcher
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
imagePath = 'C:/Users/EPLab/Desktop/COCO/StitchingPlayground/Row0/'
# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
image = cv2.imread(imagePath+'row 24.jpg')

divs = 8
z = 0
height, width, channels = image.shape
H = (height/divs)+(height/divs)*0.7
print(height)
for i in range(0,divs+2):
    z = z+1
    print(z,((i*H)/2),(H+(i*H)/2))
    imgTemp = image[int((i*H)/2):int(H+(i*H)/2),0:width]
    if z<10:
        cv2.imwrite('Sub0'+str(z)+'.jpg', imgTemp)
    else:
        cv2.imwrite('Sub'+str(z)+'.jpg', imgTemp)