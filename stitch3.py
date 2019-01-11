#
# python stitch2.py --images C:/Users/EPLab/Desktop/COCO/StitchingTest/Row2 --output output.png --crop 1
#

"""
Created on Sun Dec 23 00:47:58 2018

@author: EPLab
"""

def RowStitchFunc (str, path, ScanPath):
    # import the necessary packages
    from imutils import paths
    import imutils
    import cv2
    import os
    
    # grab the paths to the input images and initialize our images list
    print("[INFO] loading images...")
    imagePaths = sorted(list(paths.list_images(path)))
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
    
    (status, stitched) = stitcher.stitch(images)
    
    # if the status is '0', then OpenCV successfully performed image stitching
    if status == 0:
    
        # write the output stitched image to disk
    	cv2.imwrite(os.path.join(ScanPath,str), stitched)
    
    	# display the output stitched image to our screen
    	#cv2.imshow("Stitched", stitched)
    	#cv2.waitKey(0)
    
    # otherwise the stitching failed, likely due to not enough keypoints)
    # being detected
    else:
    	print("[INFO] image stitching failed ({})".format(status))