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
imageA = imagePath+'captureX0Y0P0000.jpg'
imageB = imagePath+'captureX2Y0P0001.jpg'
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)