# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 17:32:29 2018

@author: EPLab
"""

import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import time
import imutils
import csv

IMAGE_NAME = "test.png"
PATH_TO_IMAGE = 'C:/Users/EPLab/Desktop/COCO/BIPP/'+IMAGE_NAME

image = cv2.imread(PATH_TO_IMAGE)



#subImage_5	0	3084	0.3093025	0.8407979	0.4374405	0.878887

'''
subImage_1	darkHole	0	0	0.7666964	0.69233835	0.8690026	0.7372571
subImage_2	darkHole	0	771	0.7106138	0.65271086	0.85311335	0.696194
subImage_2	darkHole	0	771	0.36855194	0.9025578	0.4829329	0.9396517
subImage_3	darkHole	0	1542	0.71649045	0.13539553	0.8617867	0.18236125
subImage_3	darkHole	0	1542	0.71832526	0.6376682	0.84115547	0.6797707
subImage_3	darkHole	0	1542	0.72262555	0.8853638	0.85906875	0.9248197
subImage_4	darkHole	0	2313	0.6843539	0.616828	0.81612384	0.6542689
subImage_4	darkHole	0	2313	0.36873087	0.36705747	0.48633265	0.4043621
subImage_4	darkHole	0	2313	0.3407029	0.8624675	0.4849731	0.90390486
subImage_5	darkHole	0	3084	0.6750291	0.8421605	0.80675834	0.8822556
subImage_5	darkHole	0	3084	0.3093025	0.8407979	0.4374405	0.878887
subImage_5	darkHole	0	3084	0.7172496	0.6001145	0.8451747	0.63957393
subImage_6	darkHole	0	3855	0.69342834	0.3342945	0.8178197	0.3673614
subImage_6	darkHole	0	3855	0.7284521	0.5772029	0.84799147	0.61987203

'''
im_width = 771
im_height = 496

#box = [0,0,0.7666964,0.69233835, 0.8690026, 0.7372571]
#box = [0, 1542, 0.71832526, 0.6376682, 0.84115547, 0.6797707]
#box = [0, 3855, 0.7284521, 0.5772029, 0.84799147, 0.61987203]
box = [0,6168,0.28105357	,0.26173064	,0.42827743	,0.31644186]
#SubImage Width and Height
absCoordX = box[0]
absCoordY = box[1]
xmin = box[2]
ymin = box[3]
xmax = box[4]
ymax = box[5]

margin = 0
(left, right, top, bottom) = (ymin*im_width-margin, ymax*im_width+margin, xmin * im_height-margin, xmax * im_height+margin)


print(left, right, top, bottom)
image2 = image[absCoordX+int(top):absCoordX+int(bottom), int(left)+absCoordY:int(right)+absCoordY]
#cv2.imshow("image2", image2)

#image3 = image[absCoordX:absCoordX+im_height, absCoordY:absCoordY+im_width]
image3 = image
#Bounding Box Width and Height
w = right-left
h = bottom-top

# Enclosing Circle
cX = absCoordX+top+(h/2)
cY = absCoordY+left+(w/2)
radius = h//2

image3 = cv2.circle(image3, (int(cY), int(cX)), int(radius), (0, 0, 255), 3)
cv2.imshow("image3", imutils.resize(image3, width= 600))
cv2.waitKey(0)
