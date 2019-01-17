# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 11:57:07 2019

@author: EPLab
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 00:19:36 2018

@author: EPLab
"""

def PlotHolesFunc (path):
    import os
    import matplotlib.pyplot as plt
    import csv
    import numpy
    import statistics
    import seaborn as sns
    
    newPath = path + "/ResultsFigures"
    try:  
        os.mkdir(newPath)
    except OSError:  
        print ("Creation of the directory %s failed" % newPath)
    else:  
        print ("Successfully created the directory %s" % newPath)
    
    AbsoluteX = []
    AbsoluteY = []
    Luminance = []
    Radius = [] 
    BBW = []
    BBH = []
    BBWH = []
    BBA = []
    numPix = []
    Density = []
    conv = 125 # Pixles per mm
    
    with open(os.path.join(path ,'channels.csv'), 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                AbsoluteX.append(float(row["cmcX"]))
                AbsoluteY.append(float(row["cmcY"]))
                if(float(row["luminance"]) >= 100):
                    Luminance.append(100)
                elif(100 >= float(row["luminance"]) >= 50):
                    Luminance.append(50)
                else:
                    Luminance.append(0)
                #Luminance.append(int(round(float(row["luminance"]))))
                #Luminance.append(int(round(float(row["luminance"]),4)))
                Radius.append(float(row["width"]))
                BBW.append(float(row["height"]))
            except AttributeError:
                print("No Entry")
    print(Luminance)
    #r = 0.01#0.03
    #AbsoluteXX, AbsoluteYY = filter(AbsoluteX, AbsoluteY,r)

#    print(statistics.mean(Luminance))
#    print(statistics.stdev(Luminance))
#    print(statistics.mean(BBWH))
#    print(statistics.stdev(BBWH))
#    print(statistics.mean(Density))
#    print(statistics.stdev(Density))
    
    
    
    
    f1 = plt.figure(1)
    #plt.scatter(AbsoluteX, AbsoluteY, s=1)
    plt.scatter(AbsoluteX, AbsoluteY, s=10, c=Luminance, cmap='winter')
    plt.colorbar()
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
#    plt.xlim(10,15)  
#    plt.ylim(33,44)  
    #plt.show()
    
    '''
    f2 = plt.figure(2)
    sns.set()
    #sns.heatmap(AbsoluteX, AbsoluteY, Luminance)
    subdivide = 25
    X = []
    Y = []
    Lum = []
    LumTemp = []
    XTemp = []
    YTemp = []
    for j in range(0,70//subdivide):
        for i in range(0,len(AbsoluteX)):
            if(AbsoluteX[i] > subdivide*(j+1) and  AbsoluteX[i] >= subdivide*j and subdivide*(j+1) > AbsoluteY[i] and AbsoluteY[i] >= subdivide*j):
                LumTemp.append(Luminance[i])
                XTemp.append(AbsoluteX[i])
                YTemp.append(AbsoluteY[i])
                print(LumTemp)
        Lum.append(statistics.mean(LumTemp))
        X.append(statistics.mean(XTemp))
        Y.append(statistics.mean(YTemp))

    #sns.heatmap((AbsoluteY, AbsoluteX, Luminance), annot=False)
    sns.heatmap((Y, X, Lum), annot=False)

    plt.axes(projction='3d')
    plt.scatter(AbsoluteX, AbsoluteY, Luminance, c=Luminance, cmap='viridis')
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
#    plt.xlim(10,15)  
#    plt.ylim(33,44)  
    '''
    plt.show()
    
#    f2 = plt.figure(2)
#    plt.scatter(BBA, Density, s=1)
#    # calc the trendline
#    z = numpy.polyfit(BBA, Density, 1)
#    p = numpy.poly1d(z)
#    plt.plot(BBA,p(BBA),"r--")
#    # the line equation:
#    equation = 'y='+ str(z[0]) +' x + '+ str(z[1])
#    plt.xlabel("Bounding Rectangle Area [mm^2]")
#    plt.ylabel("Density [%]")
#    plt.figtext(0.4,.3, equation)
#    plt.show(block=False)
##    
#    f3 = plt.figure(3)
#    plt.scatter(AbsoluteX, Density, s=1)
#    # calc the trendline
#    z = numpy.polyfit(AbsoluteX, Density, 1)
#    p = numpy.poly1d(z)
#    plt.plot(AbsoluteX,p(AbsoluteX),"r--")
#    # the line equation:
#    equation = 'y='+ str(z[0]) +' x + '+ str(z[1])
#    plt.xlabel("Absolute X [mm]")
#    plt.ylabel("Density [%]")
#    plt.figtext(0.4,.3, equation)
#    plt.show(block=False)
#    
#    f4 = plt.figure(4)
#    plt.scatter(BBA, numPix, s=1)
#    # calc the trendline
#    z = numpy.polyfit(BBA, numPix, 1)
#    p = numpy.poly1d(z)
#    plt.plot(BBA,p(BBA),"r--")
#    # the line equation:
#    equation = 'y='+ str(z[0]) +' x + '+ str(z[1])
#    plt.xlabel("Bounding Rectangle Area [mm^2]")
#    plt.ylabel("Number of Pixels per Hole [px]")
#    plt.figtext(0.4,.3, equation)
#    plt.show(block=False)
#    
#    f5 = plt.figure(5)
#    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
#    plt.hist(Density,bins=numpy.linspace(0.7,1,20), zorder = 3)
#    plt.xlabel("Density [%]")
#    plt.ylabel("Frequency")
#    plt.show(block=False)
#    
#    f6 = plt.figure(6)
#    plt.scatter(BBW, BBH, s=.5)
#    plt.xlabel("Bounding Rectangle Width [mm]")
#    plt.ylabel("Bounding Rectangle Height [mm]")
#    plt.show(block=False)
#    
#    f7 = plt.figure(7)
#    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
#    plt.hist(BBWH,bins=numpy.linspace(0,2,20), zorder = 3)
#    plt.xlabel("Width-to-Height Ratio [mm/mm]")
#    plt.ylabel("Frequency")
#    plt.show(block=False)
#    
#    f8 = plt.figure(8)
#    plt.scatter(AbsoluteX, Luminance, s=.5)
#    plt.xlabel("Absolute X [mm]")
#    plt.ylabel("Luminance")
#    plt.show(block=False)
#    
#    f9 = plt.figure(9)
#    plt.scatter(AbsoluteY, Luminance, s=.5)
#    plt.xlabel("Absolute Y [mm]")
#    plt.ylabel("Luminance")
#    plt.show(block=False)
#    
#    f10 = plt.figure(10)
#    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
#    #plt.hist(Luminance,bins=numpy.linspace(0,2,20), zorder = 3)
#    plt.hist(Luminance, zorder = 3)
#    plt.xlabel("Luminance")
#    plt.ylabel("Frequency")
#    plt.show()
    
    f1.savefig(os.path.join(newPath, "HoleLoc.jpeg") , orientation='landscape', quality=95)
#    f2.savefig(os.path.join(newPath, "BBADens.jpeg") , orientation='landscape', quality=95)
#    f3.savefig(os.path.join(newPath, "XDens.jpeg") , orientation='landscape', quality=95)
#    f4.savefig(os.path.join(newPath, "BBAPix.jpeg") , orientation='landscape', quality=95)
#    f5.savefig(os.path.join(newPath, "DensFreq.jpeg") , orientation='landscape', quality=95)
#    f6.savefig(os.path.join(newPath, "BBWBBH.jpeg") , orientation='landscape', quality=95)
#    f7.savefig(os.path.join(newPath, "BBWHFreq.jpeg") , orientation='landscape', quality=95)
#    f8.savefig(os.path.join(newPath, "XLum.jpeg") , orientation='landscape', quality=95)
#    f9.savefig(os.path.join(newPath, "YLum.jpeg") , orientation='landscape', quality=95)
#    f10.savefig(os.path.join(newPath, "LumFreq.jpeg") , orientation='landscape', quality=95)
    print('NOTE: To compare location plots, picture of array must be rotated 90d clockwise')

def filterOld(AbsoluteX, AbsoluteY, Luminance, Radius, BBW, BBH, BBWH, BBA, numPix, Density,r):
    import statistics 
    ScatterDistX = []
    ScatterDistY = []
    AbsoluteXX = []
    AbsoluteYY = []
    i = 0
    while (i<=len(AbsoluteX)-1):
        j = 0
        while (j<=len(AbsoluteX)-1):
            if i != j and abs(AbsoluteX[i]-AbsoluteX[j]) < r and abs(AbsoluteY[i]-AbsoluteY[j]) < r:
            #if i != j and i-12<=j<=i+12 and ((abs(AbsoluteX[i]-AbsoluteX[j]))**2 + (abs(AbsoluteY[i]-AbsoluteY[j]))**2)**0.5 < r:
                    ScatterDistX.append(abs(AbsoluteX[i]-AbsoluteX[j]))
                    ScatterDistY.append(abs(AbsoluteY[i]-AbsoluteY[j]))
                    #AbsoluteX[i] = ((AbsoluteX[i]+AbsoluteX[j])/2)
                    #AbsoluteY[i] = ((AbsoluteY[i]+AbsoluteY[j])/2)
                    AbsoluteXX.append(((AbsoluteX[i]+AbsoluteX[j])/2))
                    AbsoluteYY.append((AbsoluteY[i]+AbsoluteY[j])/2)
                    
#                    AbsoluteX.remove(AbsoluteX[j])
#                    AbsoluteY.remove(AbsoluteY[j])
#                    
#                    Luminance.remove(Luminance[j])
#                    Radius.remove(Radius[j])
#                    BBW.remove(BBW[j])
#                    BBH.remove(BBH[j])
#                    BBWH.remove(BBWH[j])
#                    BBA.remove(BBA[j])
#                    numPix.remove(numPix[j])
#                    Density.remove(Density[j])
                    #ScatterDist.append(((abs(AbsoluteX[i]-AbsoluteX[j]))**2 + (abs(AbsoluteY[i]-AbsoluteY[j]))**2)**0.5)
            else:
                AbsoluteXX.append(AbsoluteX[i])
                AbsoluteYY.append(AbsoluteY[i]) 
            j=j+1
        i=i+1
    print(statistics.mean(ScatterDistX))
    print(statistics.mean(ScatterDistY))
    #print(ScatterDist)
    return AbsoluteXX, AbsoluteYY, Luminance, Radius, BBW, BBH, BBWH, BBA, numPix, Density
    print('NOTE: To compare location plots, picture of array must be rotated 90d clockwise')
    
def filter(AbsoluteX, AbsoluteY, r):
    import statistics 
    ScatterDistX = []
    ScatterDistY = []
    AbsoluteXX = []
    AbsoluteYY = []
    i = 0
    while (i<=len(AbsoluteX)-1):
        j = 0
        while (j<=len(AbsoluteX)-1):
            if i != j and abs(AbsoluteX[i]-AbsoluteX[j]) < r and abs(AbsoluteY[i]-AbsoluteY[j]) < r:
                    ScatterDistX.append(abs(AbsoluteX[i]-AbsoluteX[j]))
                    ScatterDistY.append(abs(AbsoluteY[i]-AbsoluteY[j]))
            j=j+1
        i=i+1
    print(statistics.mean(ScatterDistX))
    print(statistics.mean(ScatterDistY))
    return AbsoluteXX, AbsoluteYY

#    
#import argparse
#
## construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--path", required=True,
#	help="path")
#args = vars(ap.parse_args())
#
#path = "C:/Users/EPLab/Desktop/COCO/"+args["path"]
#
#PlotHolesFunc (path)