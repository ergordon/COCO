# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:23:05 2018

@author: EPLab
"""
import csv
from lightIntense import lightIntenseFunc
from PlotHoles import PlotHolesFunc
import argparse
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--path", required=True,
	help="path")
args = vars(ap.parse_args())

path = "C:/Users/EPLab/Desktop/COCO/"+args["path"]

#---------------#
# NEW CODE HERE #
#---------------#

newPath = path + "/ImageResults"
try:  
    os.mkdir(newPath)
except OSError:  
    print ("Creation of the directory %s failed" % newPath)
else:  
    print ("Successfully created the directory %s" % newPath)

#---------------#

with open(os.path.join(path,'holes.csv'),'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["SourceImage","Relative X","Relative Y","Radius","Absolute X","Absolute Y","Luminance","Number of Pixels Detected","Rectangle Bounding Width","Rectangle Bounding Height","Rectangle Bounding Area"])

from numpy import genfromtxt
yyy = genfromtxt(os.path.join(path,'YLocs.csv'), delimiter=',')
xxx = genfromtxt(os.path.join(path,'XLocs.csv'), delimiter=',')

num_img_max = sum(1 for row in yyy)
num_img_init = 0
for num_img in range(num_img_init,num_img_max,1):
    if ( num_img < 10 ):
        lightIntenseFunc("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P000"+str(num_img)+".jpg", path)
    elif ( 10 <= num_img <= 99 ):
        lightIntenseFunc("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P00"+str(num_img)+".jpg", path)
    elif ( 100 <= num_img <= 999 ):
        lightIntenseFunc("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P0"+str(num_img)+".jpg", path)
    else:
        lightIntenseFunc("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P"+str(num_img)+".jpg", path)
        
# Wait here until printing is finished to close serial port and file.
input("  Press <Enter> to move forward with the results")
PlotHolesFunc (path)
