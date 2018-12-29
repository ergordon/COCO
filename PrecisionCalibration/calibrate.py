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
from lightIntense import lightIntenseFunc
from PlotHoles import PlotHolesFunc
import csv

def removeComment(string):
	if (string.find(';')==-1):
		return string
	else:
		return string[:string.index(';')]
 
filename = "calibrate"
## Make new Directories

path = "C:/Users/EPLab/Desktop/COCO/"+str(filename)
try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s" % path)


## Create G-Code File

file = open(os.path.join(path, str(filename)+".nc"), "x")

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

file.write("G04 P1 \n")
file.write("G91 \n")
file.write("G0 X4 \n")

file.write("G04 P1 \n")
file.write("G91 \n")
file.write("G0 X-1 \n")
file.write("G04 P7 \n")

for x in range(10):
    file.write("G04 P.5 \n")
    file.write("G91 \n")
    file.write("G0 X0.1 \n")
    file.write("G04 P.5 \n")
    
file.write("G04 P7 \n")
file.write("G91 \n")
file.write("G0 X1 \n")
file.write("G04 P7 \n")
file.write("G91 \n")
file.write("G0 X1 \n")
file.write("G04 P7 \n")
file.write("G91 \n")
file.write("G0 X1 \n")
file.write("G04 P7 \n")
file.write("G28 ( All Axis Home) \n")
file.close() 

# Open serial port
s = serial.Serial('COM6',115200)
print('Opening Serial Port')
 
# Open g-code file
#f = open(str(filename)+".nc",'r');
f = open(os.path.join(path+"/" ,str(filename)+".nc"),'r');

print ('Opening gcode file')
 
# Wake up 
time.sleep(2)   # Wait for Printrbot to initialize
s.flushInput()  # Flush startup text in serial input
print ('Sending gcode')

# Stream g-code
for line in f:
    l = removeComment(line)
    l = l.strip() # Strip all EOL characters for streaming
    if  (l.isspace()==False and len(l)>0) :
        print ('Sending: ' + l)
    s.write(str.encode(l + '\n')) # Send g-code block
    grbl_out = s.readline() # Wait for response with carriage return
    print (' : ' + str(grbl_out.strip()))


# Close file and serial port
f.close()
s.close()
