# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:42:04 2019

@author: EPLab
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:47:55 2018

@author: Emilio Gordon
"""

def ChannelInfoFunc (path,PATH_TO_IMAGE,subImage,class_name, absCoordX,absCoordY,im_width,im_height,xmin,ymin,xmax,ymax, convX, convY,z):
    # import the necessary packages
    from imutils import contours
    from skimage import measure
    import numpy as np
    import imutils
    import cv2
    import csv
    import os

    newPath = path + "/Channels"
    
        
    image = cv2.imread(PATH_TO_IMAGE)
    image = cv2.flip(image, 0)
    with open(os.path.join(path,'Channels.csv'),'a',newline='') as csvfile:
        wrtr = csv.writer(csvfile, delimiter=',', quotechar='"')
        csvfile.flush() # whenever you want, and/or
    
        marginW = .2
        marginH = .1
        # Get Channel Coordinates in px
        overlap = 0
        (left, right, top, bottom) = (ymin*(im_width+overlap), ymax*(im_width+overlap), xmin * (overlap+im_height), xmax * (overlap+im_height))
        
        #Bounding Box Width and Height
        w = right-left
        h = bottom-top
        
        # Enclosing Circle
        cX = absCoordX+top+(h/2)
        cY = absCoordY+left+(w/2)
        
        # Look at just the channel
        image2 = image[absCoordX+int(top)+int(marginW*w):absCoordX+int(bottom)-int(marginW*w), int(left)+absCoordY+int(marginH*h):int(right)+absCoordY-int(marginH*h)]
        
        try:
            test = cv2.cvtColor(image2, cv2.COLOR_BGR2LAB)
            l_channel,a_channel,b_channel = cv2.split(test)
            lMean = np.mean(l_channel)
            if(lMean >= 90):
                cv2.imwrite(os.path.join(newPath+"/Light",subImage+'_channel_'+str(z)+'_LUM_'+str(int(round(lMean)))+'.jpg'), image2)
            elif(90 > lMean >= 45):
                cv2.imwrite(os.path.join(newPath+"/Grey",subImage+'_channel_'+str(z)+'_LUM_'+str(int(round(lMean)))+'.jpg'), image2)
            else:
                cv2.imwrite(os.path.join(newPath+"/Dark",subImage+'_channel_'+str(z)+'_LUM_'+str(int(round(lMean)))+'.jpg'), image2)
        except ValueError:
            pass

        # Look at subImage
        #image3 = image[absCoordX:absCoordX+im_height, absCoordY:absCoordY+im_width]
        '''
        if(xmax == 1 or ymax == 1):
            pass
        else:
            wrtr.writerow([subImage,class_name+str(z),absCoordX,absCoordY,xmin,ymin,xmax,ymax, cY, cX, convY*cY, convX*cX, lMean, w*convY, h*convX])
            csvfile.flush()
        '''
        wrtr.writerow([subImage,class_name+str(z),absCoordX,absCoordY,xmin,ymin,xmax,ymax, cY, cX, convY*cY, convX*cX, lMean, w*convY, h*convX])
        csvfile.flush()