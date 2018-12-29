# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:53:58 2018

@author: Emilio Gordon
"""

import serial
from serial import Serial
import time
import cv2
import numpy as np
import os
import csv


filename = "Tester"
print("Must be even: Ex. 7x3.4")
length = 1
width = .3
print("Your G-Code will output as " + str(filename) + ".nc for your " +str(length)+"x"+str(width)+" cm array.")

## Make new Directories

path = "C:/Users/EPLab/Desktop/COCO/"+str(filename)
try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)
    
newPath = path + "/ImageResults"
try:  
    os.mkdir(newPath)
except OSError:  
    print ("Creation of the directory %s failed" % newPath)
else:  
    print ("Successfully created the directory %s" % newPath)

## Create G-Code File

file = open(os.path.join(path, str(filename)+".nc"), "x")

xStep = 1
yStep = 2

length = (float(length)*10)+xStep*2
width = (float(width)*10)+yStep*2


file.write("G28 ( All Axis Home) \n") 
file.write("G21 G90 G40 (Set To mm, set to absolute position, No compensation ) \n")
file.write("$100=397.34 (x, step/mm)")
file.write("$101=397.34 (y, step/mm)")
## STUFF TO ADD TO COCO
file.write("$110=500 (x, mm/min)")
file.write("$111=500 (y, mm/min)")
file.write("$120=5 (x, mm/s^2)")
file.write("$121=5 (y, mm/s^2)")
##
file.write("G0 F1500 \n") 
file.write("G0 X0 Y0 Z0 ( Move to this location ) \n") 

xx = 0
yy = 0
xxx = []
yyy = []
for y in range(0, int(width), int(yStep)):
    
    PathTemp = newPath + "/Row"+str(yy*yStep)
    try:  
        os.mkdir(PathTemp)
    except OSError:  
        print ("Creation of the directory %s failed" % PathTemp)
    else:  
        print ("Successfully created the directory %s" % PathTemp)
        
    yy = yy+1    

    for x in range(0, int(length), int(xStep)):
        yyy.extend([y])
        xx=xx+1;
        if yy % 2 == 0 and yy != 0:
            if xx == (int(length)/xStep):
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 Y-2 \n")
                xxx.extend([length-xxx[xx-1]])
                xx = 0
            else:
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 X1 \n")
                xxx.extend([length-xxx[xx-1]])
        else:
            if xx == (int(length)/xStep):
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 Y-2 \n")
                xxx.extend([x])
                xx = 0
            else:
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 X-1 \n")
                xxx.extend([x])

file.write("G28 ( All Axis Home) \n")
file.close() 
a = np.asarray(xxx)
b = np.asarray(yyy)
np.savetxt(os.path.join(path+"/" ,"XLocs.csv"), a, delimiter=",")
np.savetxt(os.path.join(path+"/" ,"YLocs.csv"), b, delimiter=",")

print("at end  " + str(yy))