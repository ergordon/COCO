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
    import pandas as pd
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
    LuminanceExact = []
    Width = []
    Height = []
    Area = []
    HtW = []
    with open(os.path.join(path ,'Channels.csv'), 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                AbsoluteY.append(float(row["cmcX"]))
                AbsoluteX.append(float(row["cmcY"]))
                if(float(row["luminance"]) >= 100):
                    Luminance.append(100)
                elif(100 > float(row["luminance"]) >= 65):
                    Luminance.append(50)
                else:
                    Luminance.append(0)
                LuminanceExact.append(int(round(float(row["luminance"]))))
                #Luminance.append(int(round(float(row["luminance"]),4)))
                Width.append(float(row["width"]))
                Height.append(float(row["height"]))
                Area.append(float(row["width"])*float(row["height"]))
                HtW.append(float(row["height"])/float(row["width"]))
            except AttributeError:
                print("No Entry")

    #r = 0.01#0.03
    #AbsoluteXX, AbsoluteYY = filter(AbsoluteX, AbsoluteY,r)

    print(statistics.mean(Luminance))
    print(statistics.stdev(Luminance))
    print(statistics.mean(Area))
    print(statistics.stdev(Area))
    print(statistics.mean(HtW))
    print(statistics.stdev(HtW))
    
    f1 = plt.figure(1)
    #plt.scatter(AbsoluteX, AbsoluteY, s=1)
    plt.scatter(AbsoluteX, AbsoluteY, s=10, c=Luminance, cmap='winter')
    plt.colorbar()
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]") 
    plt.show(block=False)
   
    f2 = plt.figure(2)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(LuminanceExact,bins=numpy.linspace(0,200,20), zorder = 3)
    plt.xlabel("Luminance")
    plt.ylabel("Frequency")
    plt.show(block=False)
    
    f3 = plt.figure(3)
    heatmap, xedges, yedges = numpy.histogram2d(AbsoluteX, AbsoluteY, bins=50)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    plt.colorbar()
    plt.show(block=False)
    
    f4 = plt.figure(4)
    x = AbsoluteX
    y = AbsoluteY
    z = LuminanceExact
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    subDivide = 5
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower')

    # Loop over data dimensions and create text annotations.
    for i in range(1,35,subDivide):
        for j in range(1,70,subDivide):
            plt.text(i+(subDivide/2.5), j+(subDivide/2.5), str(int(round(res[i][j]))),
                           ha="center", va="center", color="w")
            
    plt.colorbar()
    plt.xticks(binsx)
    plt.yticks(binsy)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    plt.title('Luminosity Heatmap')
    plt.grid(False)
    plt.show(block=False)
    
    
    f5 = plt.figure(5)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(Area,bins=numpy.linspace(0,.075,20), zorder = 3)
    plt.xlabel("Area")
    plt.ylabel("Frequency")
    plt.show(block=False)
    
    
    f6 = plt.figure(6)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(HtW,bins=numpy.linspace(0,1,20), zorder = 3)
    plt.xlabel("Height:Width")
    plt.ylabel("Frequency")
    plt.show(block=False)
    
    
    f7 = plt.figure(7)
    x = AbsoluteX
    y = AbsoluteY
    z = Area
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    subDivide = 5
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower')
    plt.colorbar()
    plt.xticks(binsx)
    plt.yticks(binsy)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    plt.title('Area Heatmap')
    plt.grid(False)
    plt.show(block=False)
    
    
    f8 = plt.figure(8)
    x = AbsoluteX
    y = AbsoluteY
    z = HtW
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    subDivide = 5
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower')    
    plt.colorbar()
    plt.xticks(binsx)
    plt.yticks(binsy)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    plt.title('Height: Width Heatmap')
    plt.grid(False)
    plt.show(block=False)

    f9 = plt.figure(9)
    plt.scatter(AbsoluteX, AbsoluteY, s=1)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]") 
    plt.show()
    
    f1.savefig(os.path.join(newPath, "ChannelLocationwLuminoisty.jpeg") , orientation='landscape', quality=95)
    f2.savefig(os.path.join(newPath, "LuminosityOverallDistribution.jpeg") , orientation='landscape', quality=95)
    f3.savefig(os.path.join(newPath, "ChannelDensity.jpeg") , orientation='landscape', quality=95)
    f4.savefig(os.path.join(newPath, "LuminosityHeatMap.jpeg") , orientation='landscape', quality=95)
    f5.savefig(os.path.join(newPath, "AreaHistorgram.jpeg") , orientation='landscape', quality=95)
    f6.savefig(os.path.join(newPath, "HeighttoWidthHistogram.jpeg") , orientation='landscape', quality=95)
    f7.savefig(os.path.join(newPath, "AreaHeatmap.jpeg") , orientation='landscape', quality=95)
    f8.savefig(os.path.join(newPath, "HeighttoWidthHeatmap.jpeg") , orientation='landscape', quality=95)
    f9.savefig(os.path.join(newPath, "ChannelLocation.jpeg") , orientation='landscape', quality=95)
#    f10.savefig(os.path.join(newPath, "LumFreq.jpeg") , orientation='landscape', quality=95)