# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:53:58 2018

@author: Emilio Gordon
"""

import serial
import time
import cv2

def removeComment(string):
	if (string.find(';')==-1):
		return string
	else:
		return string[:string.index(';')]
    
cap = cv2.VideoCapture(1)
def TakeImage(z):
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    cv2.imshow('frame', rgb)
    if ( z < 10 ):
        cv2.imwrite("capture000"+str(z)+".jpg", frame)
    elif (10 <= z <= 99):
        cv2.imwrite("capture00"+str(z)+".jpg", frame)
    elif (100 <= z <= 999):
        cv2.imwrite("capture0"+str(z)+".jpg", frame)
    else:
        cv2.imwrite("capture"+str(z)+".jpg", frame)
        
    
filename = input("Enter Desired File Name: ")
length = input("Enter Array Length [cm] (X-axis): ")
width = input("Enter Array Width [cm] (Y-axis): ")
print("Your G-Code will output as " + str(filename) + ".nc for your " +str(length)+"x"+str(width)+" cm array.")


file = open(str(filename)+".nc", "x")

xStep = 2
yStep = 2

length = (int(length)*10)+xStep*2
width = (int(width)*10)+yStep*2


print("Your Panorama Matrix will have " + str(int(length)/xStep) + "rows")


file.write("G28 ( All Axis Home) \n") 
file.write("G21 G90 G40 (Set To mm, set to absolute position, No compensation ) \n") 
file.write("G0 F1500 \n") 
file.write("G0 X0 Y0 Z0 ( Move to this location ) \n") 

xx = 0
yy = 0

for y in range(1, int(width), yStep):
    yy = yy+1
    for x in range(1, int(length), xStep):
        xx=xx+1;
        if yy % 2 == 0 and yy != 0:
            if xx == (int(length)/xStep):
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 Y-2 \n")
                xx = 0
            else:
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 X2 \n")
        else:
            if xx == (int(length)/xStep):
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 Y-2 \n")
                xx = 0
            else:
                file.write("G04 P1 \n")
                file.write("G04 P0.5 \n")
                file.write("G91 \n")
                file.write("G0 X-2 \n")

file.write("G28 ( All Axis Home) \n")
file.close() 

# Open serial port
s = serial.Serial('COM6',115200)
print('Opening Serial Port')
 
# Open g-code file
f = open(str(filename)+".nc",'r');
print ('Opening gcode file')
 
# Wake up 
time.sleep(2)   # Wait for Printrbot to initialize
s.flushInput()  # Flush startup text in serial input
print ('Sending gcode')

z = 0
# Stream g-code
for line in f:
    l = removeComment(line)
    l = l.strip() # Strip all EOL characters for streaming
    if  (l.isspace()==False and len(l)>0) :
        print ('Sending: ' + l)
        if(l == "G04 P0.5"):
            TakeImage(z)
            z=z+1
    s.write(str.encode(l + '\n')) # Send g-code block
    grbl_out = s.readline() # Wait for response with carriage return
    print (' : ' + str(grbl_out.strip()))
 
# Wait here until printing is finished to close serial port and file.
input("  Press <Enter> to exit.")
 
# Close file and serial port
f.close()
s.close()
cap.release()

