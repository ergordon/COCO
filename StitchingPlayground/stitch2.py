#
# python stitch2.py --images C:\Users\EPLab\Desktop\COCO\testZoomedOutX2mm\ImageResults\Row0 --output Row0.png
#

"""
Created on Sun Dec 23 00:47:58 2018

@author: EPLab
"""
# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
	help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True,
	help="path to the output image")
args = vars(ap.parse_args())

# grab the paths to the input images and initialize our images list
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []

# loop over the image paths, load each one, and add them to our
# images to stich list

### Setting for ZoomOut
#
## python stitch2.py --images C:\Users\EPLab\Desktop\COCO\testZoomedOut\ImageResults\Row0 --output Row0.png
#for imagePath in imagePaths:
#	image = cv2.imread(imagePath)
#	image=cv2.transpose(image)
#	image=cv2.flip(image,flipCode=1)
#	image=imutils.resize(image, width=400)
#	images.append(image)


### Settings for ZoomOutX2mm (Does not work for row2)
#'''
## python stitch2.py --images C:/Users/EPLab/Desktop/COCO/testZoomedOutX2mm/ImageResults/Row2 --output Row2.png
#for imagePath in imagePaths:
#	image = cv2.imread(imagePath)
#	#image=cv2.transpose(image)
#	#image=cv2.flip(image,flipCode=1)
#	#image=imutils.resize(image, width=400)
#	images.append(image)
#'''


for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	image=cv2.transpose(image)
	image=cv2.flip(image,flipCode=1)
	image=imutils.resize(image, width=400)
	
	images.append(image)

# initialize OpenCV's image sticher object and then perform the image
# stitching
print("[INFO] stitching images...")

## ZoomOut
stitcher = cv2.createStitcherScans(True)

(status, stitched) = stitcher.stitch(images)

# if the status is '0', then OpenCV successfully performed image stitching
if status == 0:
    # write the output stitched image to disk
    cv2.imwrite(args["output"], stitched)

# otherwise the stitching failed, likely due to not enough keypoints)
# being detected
else:
	print("[INFO] image stitching failed ({})".format(status))