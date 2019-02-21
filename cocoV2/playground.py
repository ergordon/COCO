# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 21:11:57 2019

@author: EPLab
"""
'''
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 50, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()
'''

### Progress Bar Playground
'''
import sys

# Print iterations progress
def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        bar_length  - Optional  : character length of bar (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()
    
      
from time import sleep

# A List of Items
items = list(range(0, 1368))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', bar_length = 45)
for i, item in enumerate(items):
    # Do stuff...
    sleep(0.01)
    # Update Progress Bar
    
    printProgressBar(i, l, prefix = 'Progress:', suffix = 'Complete', bar_length = 45)
'''

from imutils import contours
from skimage import measure
import numpy as np
import imutils
import cv2
import csv
import os
import imutils
import csv

image = cv2.imread('test5.jpg')
image = imutils.resize(image, height= 400)
cv2.imshow("image",image)

test = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
#cv2.imshow("colorchange",test)
test2=cv2.cvtColor(test, cv2.COLOR_BGR2YCrCb)
#cv2.imshow("colorchange2",test2)
img = cv2.blur(image,(3,3))
test3=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("colorchange3",test3)
'''
#lower = np.array([17,26,30])  #-- Lower range --
#upper = np.array([186,205,216])  #-- Upper range --
lower = np.array([30,26,17])  #-- Lower range --
upper = np.array([216,205,186])  #-- Upper range --
mask = cv2.inRange(test, lower, upper)
res = cv2.bitwise_and(test, test, mask= mask)  #-- Contains pixels having the gray color--
cv2.imshow('Result',res)

'''

lower = np.array([70,100,108])  #-- Lower range --
upper = np.array([210,236,239])  #-- Upper range --
mask1 = cv2.inRange(test, lower, upper)
res = cv2.bitwise_and(test, test, mask= mask1)  #-- Contains pixels having the gray color--
cv2.imshow('Result1',res)
temp=cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
mask = cv2.inRange(temp, 50, 255)#was 150
res = cv2.bitwise_and(image, image, mask= mask)  #-- Contains pixels having the gray color--
cv2.imshow('Result2',res)


#mask = cv2.inRange(test3, 50, 255)#was 150
#res = cv2.bitwise_and(image, image, mask= mask)  #-- Contains pixels having the gray color--
#cv2.imshow('Result2',res)

'''
lower = np.array([15,32,40])  #-- Lower range --
upper = np.array([150,194,218])  #-- Upper range --
mask = cv2.inRange(image, lower, upper)
res = cv2.bitwise_and(image, image, mask= mask)  #-- Contains pixels having the gray color--
cv2.imshow('Result3',res)
'''

avg_color_per_row = np.average(test, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
print(avg_color)
cv2.waitKey(0)
