# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 12:12:09 2018

@author: Emilio Gordon
"""

# Path to where my test images are stored
path = 'C:/Users/EPLab/Desktop/COCO/BIPP'
imageName = 'CompleteStitch.png'

# import the necessary packages

import imutils
import cv2
import csv
import os

# Get the image and its dimensions
image = cv2.imread(os.path.join(path,imageName))
height, width, channels = image.shape

'''
## Enforce that our image has even dimensions. 
    # If not even, remove one pixle from either end. 
if height % 2 == 0:
    pass # Even 
else:
    if width % 2 == 0:
        image = image[0:height-1,0:width]
        height, width, channels = image.shape
        pass # Even 
    else:
        image = image[0:height-1,0:width-1]
        height, width, channels = image.shape
'''

## Make the subdivisions
maxImgWidth = 850
maxImgHeight = 500

divideWidth = 2
divideHeight = 2

N = width//divideWidth
M = height//divideHeight

#while M > maxImgHeight and N > maxImgWidth:  
while M >= maxImgHeight:
    divideHeight = divideHeight + 1
    M = height//divideHeight

while N >= maxImgWidth:
    divideWidth = divideWidth + 1
    N = width//divideWidth
    
print("The input image is "+str(height)+"px by "+str(width)+" px")
print("This image will be divided into "+str(divideHeight)+" by "+str(divideWidth)+" sub-images. (height,width)")    
print("Each sub-image will be "+str(M)+"px by "+str(N)+" px")
#tiles = [image[x:x+M,y:y+N] for x in range(0,image.shape[0],M) for y in range(0,image.shape[1],N)]



#print(len(tiles))  
with open(os.path.join(path,'SubImages.csv'), mode='a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',\
                                quoting=csv.QUOTE_MINIMAL)
        
        filewriter.writerow(["SubImage Number","RelativeOriginX2Absolute",\
                             "RelativeOriginY2Absolute"])
        tiles = []
        for x in range(0,height,M):
            for y in range(0,width,N):
                tiles.append(image[x:x+M,y:y+N]) 
                filewriter.writerow(["subImage_"+str(len(tiles)),int(x),int(y)])

        
#cv2.imshow('Test',imutils.resize(image, height=1000))
#cv2.imshow('Test1',imutils.resize(tiles[0], height=500))
#cv2.imshow('Test0',tiles[200])
#cv2.imshow('Test1',tiles[300])
#cv2.imshow('Test2',tiles[400])
#cv2.imshow('Test3',imutils.resize(tiles[4], height=500))
#cv2.imshow('Test4',imutils.resize(tiles[3], height=500))
#cv2.imshow('Test3',tiles[4])
#cv2.waitKey(0)
