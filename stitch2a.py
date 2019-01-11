#
# python stitch2a.py --images C:\Users\EPLab\Desktop\COCO\testZoomedOut\ImageResults\Row0 --output Row0.png
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
for imagePath in imagePaths:
	image = cv2.imread(imagePath)
	image=cv2.transpose(image)
	image=cv2.flip(image,flipCode=1)
	images.append(image)

# initialize OpenCV's image sticher object and then perform the image
# stitching
print("[INFO] stitching images...")

stitcher = cv2.createStitcherScans(True)
StitchedImage = images[0]
cv2.imshow("Stitched", images[0])
cv2.waitKey(0)
for i in range(1, len(images)):
    cv2.imshow("Stitched", images[11])
    cv2.waitKey(0)
    print('Loop'+str(i))
    (status, Stitched) = stitcher.stitch([StitchedImage,images[11]])
    cv2.imshow("Stitched2", Stitched)
    cv2.waitKey(0)
#stitcher = cv2.createStitcherScans()




# if the status is '0', then OpenCV successfully performed image stitching
if status == 0:
    # write the output stitched image to disk
    cv2.imwrite(args["output"], stitched)

	# display the output stitched image to our screen
	#cv2.imshow("Stitched", stitched)
	#cv2.waitKey(0)

# otherwise the stitching failed, likely due to not enough keypoints)
# being detected
else:
	print("[INFO] image stitching failed ({})".format(status))