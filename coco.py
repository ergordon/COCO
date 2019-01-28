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

def removeComment(string):
	if (string.find(';')==-1):
		return string
	else:
		return string[:string.index(';')]
    
cap = cv2.VideoCapture(0)

def TakeImage(z,xxx,yyy,path):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    #cv2.imshow('frame', rgb)
    pathTemp = path + "/ImageResults/Row"+str(int(yyy[z]))
    print("TakeImage "+pathTemp)
    if ( z < 10 ):
        cv2.imwrite(os.path.join(pathTemp ,"captureP000"+str(z)+".jpg"), frame)
    elif (10 <= z <= 99):
        cv2.imwrite(os.path.join(pathTemp ,"captureP00"+str(z)+".jpg"), frame)
    elif (100 <= z <= 999):
        cv2.imwrite(os.path.join(pathTemp ,"captureP0"+str(z)+".jpg"), frame)
    else:
        cv2.imwrite(os.path.join(pathTemp ,"captureP"+str(z)+".jpg"), frame)
        
    
filename = input("Enter Desired File Name: ")
print("Must be even: Ex. 7x3.4")
length = input("Enter Array Length [cm] (X-axis): ")
width = input("Enter Array Width [cm] (Y-axis): ")
print("Your G-Code will output as " + str(filename) + ".nc for your " +str(length)+"x"+str(width)+" cm array.")

#Begin Timer
START_TIME = time.time()
    
## Make new Directories
raw_path = "C:/Users/EPLab/Desktop/COCO/"
path = raw_path+str(filename)
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
file.write("$100=397.34 (x, step/mm) \n")
file.write("$101=397.34 (y, step/mm) \n")
## STUFF TO ADD TO COCO
file.write("$110=500 (x, mm/min) \n")
file.write("$111=500 (y, mm/min) \n")
file.write("$120=5 (x, mm/s^2) \n")
file.write("$121=5 (y, mm/s^2) \n")
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
                #print(xx-1)
                xxx.extend([length-xxx[xx-1]])
                xx = 0
            else:
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 X1 \n")
                #print(xx-1)
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

# Open serial port
s = serial.Serial('COM6',115200)
print('Opening Serial Port')
 
# Open g-code file
#f = open(str(filename)+".nc",'r');
f = open(os.path.join(path+"/" ,str(filename)+".nc"),'r');

print ('Opening gcode file')
 
# Wake up 
time.sleep(2)   # Wait for CNC to initialize
s.flushInput()  # Flush startup text in serial input
print ('Sending gcode')

#zz=[]
z = 0
# Stream g-code
for line in f:
    l = removeComment(line)
    l = l.strip() # Strip all EOL characters for streaming
    if  (l.isspace()==False and len(l)>0) :
        print ('Sending: ' + l)
        if(l == "G04 P0.5"):
            TakeImage(z,xxx,yyy,path)
            z=z+1
            #zz.extend([zz])
    s.write(str.encode(l + '\n')) # Send g-code block
    grbl_out = s.readline() # Wait for response with carriage return
    print (' : ' + str(grbl_out.strip()))
    
#c = np.asarray(zz)
#np.savetxt(os.path.join(path+"/" ,"YIter.csv"), c, delimiter=",")
 
# Wait here until printing is finished to close serial port and file.
print("\n \n Use Microsoft Image Composite Editor to create a stitched image.\n Name the stitched image Stitched.jpg and place it into the project folder created at the starte of running COCO")

time.sleep(10) # Time in seconds.
# Close file and serial port
f.close()
s.close()
cap.release()

proceed = input("Press Enter when finished.")

print("Total Elapsed Time For COCO: "+ str(time.time() - START_TIME) + " sec" )
print("Test "+str(filename)+" Scanned Succesfully. "+str(length)+"x"+str(width)+" Array")
print("Perform the following task to continue: \n    1. Activate the tensorflow enviroment \n    2. Run ChannelDetection.py \n    3. Activate CNC enviroment \n    4. Run PlotHoles.py or ComparePlots.py")


