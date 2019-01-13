# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:34:43 2018

@author: Emilio Gordon
"""
# import the necessary packages
from imutils import contours
from skimage import measure
import numpy as np
import argparse
import imutils
import cv2
import csv

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the image file")
args = vars(ap.parse_args())

# load the image, convert it to grayscale, and blur it
image = cv2.imread(args["image"])
#image = imutils.resize(image, width=600)
cv2.imshow("Original Image",image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Grayed_and_Blurred",blurred)

# Find Luminance
#test = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
#l_channel,a_channel,b_channel = cv2.split(test)
#print(l_channel)
#cv2.imshow("L_Channel",l_channel)

# threshold the image to reveal light regions in the
# blurred image
#thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.threshold(blurred, 100, 200, cv2.THRESH_BINARY)[1]
cv2.imshow("Thresh",thresh)

# perform a series of erosions and dilations to remove
# any small blobs of noise from the thresholded image
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=4)
cv2.imshow("Erode_and_Dilate",thresh)
# perform a connected component analysis on the thresholded
# image, then initialize a mask to store only the "large"
# components
labels = measure.label(thresh, neighbors=8, background=0)
mask = np.zeros(thresh.shape, dtype="uint8")

# loop over the unique components
for label in np.unique(labels):
	# if this is the background label, ignore it
	if label == 0:
		continue

	# otherwise, construct the label mask and count the
	# number of pixels 
	labelMask = np.zeros(thresh.shape, dtype="uint8")
	labelMask[labels == label] = 255
	numPixels = cv2.countNonZero(labelMask)
	

	# if the number of pixels in the component is sufficiently
	# large, then add it to our mask of "large blobs"
	if numPixels > 100:
		mask = cv2.add(mask, labelMask)
# find the contours in the mask, then sort them from left to
# right
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
cnts = contours.sort_contours(cnts)[0]


## loop over the contours
with open('holes.csv', mode='a') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
	for (i, c) in enumerate(cnts):
		# draw the bright spot on the image
		(x, y, w, h) = cv2.boundingRect(c)
		print(x,y,w,h)
		((cX, cY), radius) = cv2.minEnclosingCircle(c)
		filewriter.writerow([args["image"], int(cX), int(cY), int(radius), int(cX), int(cY)])
		cv2.circle(image, (int(cX), int(cY)), int(radius), (0, 0, 255), 3)
		image2 = cv2.imread(args["image"])
		image3 = image2[y:y+h,x:x+w]
		try:
			test = cv2.cvtColor(image3, cv2.COLOR_BGR2LAB)
			l_channel,a_channel,b_channel = cv2.split(test)
			print(np.mean(l_channel))
			#cv2.imshow("L_Channel"+str(i)+str(c),l_channel)
		except ValueError:
			print("Hey lookatme")         
# show the output image
cv2.imshow("Processed Image", image)
cv2.waitKey(0)