# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 11:23:05 2018

@author: EPLab
"""
import csv
from lightIntense import lightIntenseFunc
import argparse
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--path", required=True,
	help="path")
args = vars(ap.parse_args())

path = args["path"]

with open(os.path.join(path,'holes.csv'),'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["SourceImage","Relative X","Relative Y","Radius","Absolute X","Absolute Y","Luminance"])

num_img_max = 1134
num_img_init = 1
from numpy import genfromtxt
yyy = genfromtxt(os.path.join(path,'YLocs.csv'), delimiter=',')
xxx = genfromtxt(os.path.join(path,'XLocs.csv'), delimiter=',')
for num_img in range(num_img_init,num_img_max,1):
    if ( num_img < 10 ):
        print("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P000"+str(num_img)+".jpg")
        lightIntenseFunc("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P000"+str(num_img)+".jpg", path)
    elif ( 10 <= num_img <= 99 ):
        print("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P00"+str(num_img)+".jpg")
        lightIntenseFunc("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P00"+str(num_img)+".jpg", path)
    elif ( 100 <= num_img <= 999 ):
        print("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P0"+str(num_img)+".jpg")
        lightIntenseFunc("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P0"+str(num_img)+".jpg", path)
    else:
        lightIntenseFunc("captureX"+str(int(xxx[num_img]))+"Y"+str(int(yyy[num_img]))+"P"+str(num_img)+".jpg", path)