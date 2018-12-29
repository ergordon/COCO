filename = input("Enter Desired File Name: ")
length = input("Enter Array Length [cm] (X-axis): ")
width = input("Enter Array Width [cm] (Y-axis): ")
print("Your G-Code will output as " + str(filename) + ".nc for your " +str(length)+"x"+str(width)+" cm array.")


file = open(str(filename)+".nc", "x")

length = (int(length)*10)+6
width = (int(width)*10)+6

xStep = 2
yStep = 4

file.write("G28 ( All Axis Home) \n") 
file.write("G21 G90 G40 (Set To mm, set to absolute position, No compensation ) \n") 
file.write("G0 F1500 \n") 
file.write("G0 X-85.60 Y0 Z0 ( Move to this location ) \n") 

xx = 0
yy = 0

for y in range(1, int(width), yStep):
    yy = yy+1
    for x in range(1, int(length), xStep):
        xx=xx+1;
        if yy % 2 == 0 and yy != 0:
            if xx == (int(length)/xStep):
                file.write("G04 P2 \n")
                file.write("G91 \n")
                file.write("G0 Y-4 \n")
                xx = 0
            else:
                file.write("G04 P2 \n")
                file.write("G91 \n")
                file.write("G0 X2 \n")
        else:
            if xx == (int(length)/xStep):
                file.write("G04 P2 \n")
                file.write("G91 \n")
                file.write("G0 Y-4 \n")
                xx = 0
            else:
                file.write("G04 P2 \n")
                file.write("G91 \n")
                file.write("G0 X-2 \n")

file.write("G28 ( All Axis Home) \n")
file.close() 
     