# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 08:57:10 2019

@author: EPLab
"""
# Path A is the path of the test we are running. The newest data collected.
# Path B is the path of the data we want to compare Path A to. Past data.
def ComparePlotsFunc (path, pathA, pathB):
    import os
    import matplotlib.pyplot as plt
    import csv
    import numpy
    import statistics
    import pandas as pd
    import seaborn as sns
    import argparse
    
    
    newPath = path + pathA + "/Comparison_Figures_to_"+str(pathB)
    try:  
        os.mkdir(newPath)
    except OSError:  
        print ("Creation of the directory %s failed" % newPath)
    else:  
        print ("Successfully created the directory %s" % newPath)
    
    A_AbsoluteX = []
    A_AbsoluteY = []
    A_Luminance = []
    A_LuminanceExact = []
    A_Width = []
    A_Height = []
    A_Area = []
    A_HtW = []
    A_z=0
    with open(os.path.join(path+pathA ,'Channels.csv'), 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                A_z = A_z+1
                A_AbsoluteX.append(float(row["cmcX"]))
                A_AbsoluteY.append(float(row["cmcY"]))
                if(float(row["luminance"]) >= 100):
                    A_Luminance.append(100)
                elif(100 > float(row["luminance"]) >= 65):
                    A_Luminance.append(50)
                else:
                    A_Luminance.append(0)
                A_LuminanceExact.append(int(round(float(row["luminance"]))))
                #Luminance.append(int(round(float(row["luminance"]),4)))
                A_Width.append(float(row["width"]))
                A_Height.append(float(row["height"]))
                A_Area.append(float(row["width"])*float(row["height"]))
                A_HtW.append(float(row["height"])/float(row["width"]))
            except AttributeError:
                print("No Entry")
    
    B_AbsoluteX = []
    B_AbsoluteY = []
    B_Luminance = []
    B_LuminanceExact = []
    B_Width = []
    B_Height = []
    B_Area = []
    B_HtW = []
    B_z=0
    with open(os.path.join(path+pathB ,'Channels.csv'), 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                B_z = B_z+1
                B_AbsoluteX.append(float(row["cmcX"]))
                B_AbsoluteY.append(float(row["cmcY"]))
                if(float(row["luminance"]) >= 100):
                    B_Luminance.append(100)
                elif(100 > float(row["luminance"]) >= 65):
                    B_Luminance.append(50)
                else:
                    B_Luminance.append(0)
                B_LuminanceExact.append(int(round(float(row["luminance"]))))
                #Luminance.append(int(round(float(row["luminance"]),4)))
                B_Width.append(float(row["width"]))
                B_Height.append(float(row["height"]))
                B_Area.append(float(row["width"])*float(row["height"]))
                B_HtW.append(float(row["height"])/float(row["width"]))
            except AttributeError:
                print("No Entry")
    
    ###############################################################################
    ## Print Stats
    print("\n")
    print(pathA)
    print("Mean Luminance:  " + str(round(statistics.mean(A_LuminanceExact),2)))
    print("STDe Luminance:  " + str(round(statistics.stdev(A_LuminanceExact),2)))
    print("Mean Area :  " + str(round(statistics.mean(A_Area),2)))
    print("STDe Area:  " + str(round(statistics.stdev(A_Area),2)))
    print("Mean Height-to-Width:  " + str(round(statistics.mean(A_HtW),2)))
    print("STDe Height-to-Width:  " + str(round(statistics.stdev(A_HtW),2)))
    print(str(A_z) + " Channels Detected \n \n")
    
    
    print(pathB)
    print("Mean Luminance:  " + str(round(statistics.mean(B_LuminanceExact),2)))
    print("STDe Luminance:  " + str(round(statistics.stdev(B_LuminanceExact),2)))
    print("Mean Area :  " + str(round(statistics.mean(B_Area),2)))
    print("STDe Area:  " + str(round(statistics.stdev(B_Area),2)))
    print("Mean Height-to-Width:  " + str(round(statistics.mean(B_HtW),2)))
    print("STDe Height-to-Width:  " + str(round(statistics.stdev(B_HtW),2)))
    print(str(B_z) + " Channels Detected \n \n")
    
    ###############################################################################
    ## Luminosity and Location
    fig = plt.figure("Location with Luminosity Comparison")
    plt.suptitle("Location with Luminosity Comparison")
    
    ax = fig.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    plt.scatter(A_AbsoluteX, A_AbsoluteY, s=10, c=A_Luminance, cmap='winter')
    plt.colorbar()
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]") 
    
    ax = fig.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    plt.scatter(B_AbsoluteX, B_AbsoluteY, s=10, c=B_Luminance, cmap='winter')
    plt.colorbar()
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]") 
    plt.show(block=False)
    
    ###############################################################################
    ## Luminosity Frequency
    fig1 = plt.figure("Luminosity Frequency Comparison")
    plt.suptitle("Luminosity Frequency Comparison")
    
    ax = fig1.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(A_LuminanceExact,bins=numpy.linspace(0,200,20), zorder = 3)
    plt.xlabel("Luminance")
    plt.ylabel("Frequency")
    
    ax = fig1.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(B_LuminanceExact,bins=numpy.linspace(0,200,20), zorder = 3)
    plt.xlabel("Luminance")
    plt.ylabel("Frequency")
    plt.show(block=False)
    
    ###############################################################################
    ## Channel Density
    fig2 = plt.figure("Channel Density Comparison")
    plt.suptitle("Channel Density Comparison")
    
    ax = fig2.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    heatmap, xedges, yedges = numpy.histogram2d(A_AbsoluteX, A_AbsoluteY, bins=50)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.imshow(heatmap.T, extent=extent, origin='lower', vmin=0, vmax=5)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    plt.colorbar()
    
    ax = fig2.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    heatmap, xedges, yedges = numpy.histogram2d(B_AbsoluteX, B_AbsoluteY, bins=50)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
    plt.imshow(heatmap.T, extent=extent, origin='lower', vmin=0, vmax=5)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    plt.colorbar()
    plt.show(block=False)
    
    ###############################################################################
    ## Luminosity HeatMap
    fig3 = plt.figure("Luminosity Heatmap Comparison")
    plt.suptitle("Luminosity Heatmap Comparison")
    
    ax = fig3.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    x = A_AbsoluteX
    y = A_AbsoluteY
    z = A_LuminanceExact
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    subDivide = 5
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower', vmin=50, vmax=150)
    
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
    
    ax = fig3.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    x = B_AbsoluteX
    y = B_AbsoluteY
    z = B_LuminanceExact
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower', vmin=50, vmax=150)
    
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
    plt.show(block=False)
    
    
    ###############################################################################
    ## Area Histogram
    fig4 = plt.figure("Area Frequency Comparison")
    plt.suptitle("Area Frequency Comparison")
    
    ax = fig4.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(A_Area,bins=numpy.linspace(0,.075,20), zorder = 3)
    plt.xlabel("Area")
    plt.ylabel("Frequency")
    
    ax = fig4.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(B_Area,bins=numpy.linspace(0,.075,20), zorder = 3)
    plt.xlabel("Area")
    plt.ylabel("Frequency")
    plt.show(block=False)
    
    ###############################################################################
    ## Height to Width Ratio Histogram
    fig5 = plt.figure("Height to Width Ratio Comparison")
    plt.suptitle("Height to Width Ratio Comparison")
    
    ax = fig5.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(A_HtW,bins=numpy.linspace(0,3,20), zorder = 3)
    plt.xlabel("Height:Width")
    plt.ylabel("Frequency")
    
    ax = fig5.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    plt.grid(color='r', linestyle='-', linewidth=0.25, zorder=0)
    plt.hist(B_HtW,bins=numpy.linspace(0,3,20), zorder = 3)
    plt.xlabel("Height:Width")
    plt.ylabel("Frequency")
    plt.show(block=False)
    
    
    ###############################################################################
    ## Area HeatMap
    fig6 = plt.figure("Area Heatmap Comparison")
    plt.suptitle("Area Heatmap Comparison")
    
    ax = fig6.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    x = A_AbsoluteX
    y = A_AbsoluteY
    z = A_Area
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    subDivide = 5
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower', vmin=0.01, vmax=0.05)
      
    plt.colorbar()
    plt.xticks(binsx)
    plt.yticks(binsy)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    
    ax = fig6.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    x = B_AbsoluteX
    y = B_AbsoluteY
    z = B_Area
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower', vmin=0.01, vmax=0.05)
    
    plt.colorbar()
    plt.xticks(binsx)
    plt.yticks(binsy)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    plt.show(block=False)
    
    ###############################################################################
    ## Height to Width Ratio HeatMap
    fig7 = plt.figure(" Height to Width Ratio Heatmap Comparison")
    plt.suptitle(" Height to Width Ratio Heatmap Comparison")
    
    ax = fig7.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    x = A_AbsoluteX
    y = A_AbsoluteY
    z = A_HtW
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    subDivide = 5
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower', vmin=1.5, vmax=2.5)
    
    plt.colorbar()
    plt.xticks(binsx)
    plt.yticks(binsy)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    
    ax = fig7.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    x = B_AbsoluteX
    y = B_AbsoluteY
    z = B_HtW
    df = pd.DataFrame({"x" : x, "y" : y, "z":z})
    binsx = numpy.arange(0,36,subDivide)
    binsy = numpy.arange(0,72,subDivide)
    res = df.groupby([pd.cut(df.y, binsy),pd.cut(df.x,binsx)])['z'].mean().unstack()
    plt.imshow(res, cmap='winter', 
               extent=[binsx.min(), binsx.max(),binsy.min(),binsy.max()],
               origin='lower', vmin=1.5, vmax=2.5)
    
    plt.colorbar()
    plt.xticks(binsx)
    plt.yticks(binsy)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]")
    plt.show(block=False)
    
    ###############################################################################
    ## Location Scatter
    fig8 = plt.figure("Location Comparison")
    plt.suptitle("Location Comparison")
    
    ax = fig8.add_subplot(1, 2, 1)
    ax.set_title(pathA)
    plt.scatter(A_AbsoluteX, A_AbsoluteY, s=2)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]") 
    
    ax = fig8.add_subplot(1, 2, 2)
    ax.set_title(pathB)
    plt.scatter(B_AbsoluteX, B_AbsoluteY, s=2)
    plt.xlabel("Channel X-Location [mm]")
    plt.ylabel("Channel Y-Location [mm]") 
    plt.show()
    
    fig.savefig(os.path.join(newPath, "ChannelLocationwLuminoisty.pdf") , orientation='landscape', quality=95)
    fig1.savefig(os.path.join(newPath, "LuminosityOverallDistribution.pdf") , orientation='landscape', quality=95)
    fig2.savefig(os.path.join(newPath, "ChannelDensity.pdf") , orientation='landscape', quality=95)
    fig3.savefig(os.path.join(newPath, "LuminosityHeatMap.pdf") , orientation='landscape', quality=95)
    fig4.savefig(os.path.join(newPath, "AreaHistorgram.pdf") , orientation='landscape', quality=95)
    fig5.savefig(os.path.join(newPath, "HeighttoWidthHistogram.pdf") , orientation='landscape', quality=95)
    fig6.savefig(os.path.join(newPath, "AreaHeatmap.pdf") , orientation='landscape', quality=95)
    fig7.savefig(os.path.join(newPath, "HeighttoWidthHeatmap.pdf") , orientation='landscape', quality=95)
    fig8.savefig(os.path.join(newPath, "ChannelLocation.pdf") , orientation='landscape', quality=95)
    #fig9.savefig(os.path.join(newPath, "LumFreq.jpeg") , orientation='landscape', quality=95)
