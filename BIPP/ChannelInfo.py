# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:47:55 2018

@author: Emilio Gordon
"""

def ChannelInfoFunc (PATH_TO_IMAGE,subImage,class_name, absCoordX,absCoordY,im_width,im_height,xmin,ymin,xmax,ymax, convX, convY,z):
    # import the necessary packages
    from imutils import contours
    from skimage import measure
    import numpy as np
    import imutils
    import cv2
    import csv
    import os
    
    path = os.getcwd()
    newPath = path + "/Channels"
    
        
    image = cv2.imread(PATH_TO_IMAGE)
    with open(os.path.join(os.getcwd(),'Channels.csv'),'a',newline='') as csvfile:
        wrtr = csv.writer(csvfile, delimiter=',', quotechar='"')
        csvfile.flush() # whenever you want, and/or
    
        margin = 0
        
        # Get Channel Coordinates in px
        (left, right, top, bottom) = (ymin*im_width-margin, ymax*im_width+margin, xmin * im_height-margin, xmax * im_height+margin)
        
        # Look at just the channel
        image2 = image[absCoordX+int(top):absCoordX+int(bottom), int(left)+absCoordY:int(right)+absCoordY]
        
        try:
            test = cv2.cvtColor(image2, cv2.COLOR_BGR2LAB)
            l_channel,a_channel,b_channel = cv2.split(test)
            lMean = np.mean(l_channel)
            if(lMean >= 100):
                cv2.imwrite(os.path.join(newPath+"/Light",subImage+'_channel_'+str(z)+'_LUM_'+str(int(round(lMean)))+'.jpg'), image2)
            elif(100 > lMean >= 65):
                cv2.imwrite(os.path.join(newPath+"/Grey",subImage+'_channel_'+str(z)+'_LUM_'+str(int(round(lMean)))+'.jpg'), image2)
            else:
                cv2.imwrite(os.path.join(newPath+"/Dark",subImage+'_channel_'+str(z)+'_LUM_'+str(int(round(lMean)))+'.jpg'), image2)
        except ValueError:
            pass

        # Look at subImage
        #image3 = image[absCoordX:absCoordX+im_height, absCoordY:absCoordY+im_width]
        
        
        #Bounding Box Width and Height
        w = right-left
        h = bottom-top
        
        # Enclosing Circle
        cX = absCoordX+top+(h/2)
        cY = absCoordY+left+(w/2)
        
        
        wrtr.writerow([subImage,class_name+str(z),absCoordX,absCoordY,xmin,ymin,xmax,ymax, cX, cY, convX*cX, convY*cY, lMean, w*convY, h*convX])
        csvfile.flush()