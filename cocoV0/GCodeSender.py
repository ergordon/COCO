
"""\
Simple g-code streaming script
"""
 
import serial
import time


def removeComment(string):
	if (string.find(';')==-1):
		return string
	else:
		return string[:string.index(';')]
 
# Open serial port
s = serial.Serial('COM6',115200)
print('Opening Serial Port')

filename = 'testerMove.nc'
 
# Open g-code file
f = open("C:/Users/EPLab/Desktop/3AxisThrusterArrayInterrogator/GCodes/"+str(filename),'r');
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
 
# Wait here until printing is finished to close serial port and file.
input("  Press <Enter> to exit.")
 
# Close file and serial port
f.close()
s.close()