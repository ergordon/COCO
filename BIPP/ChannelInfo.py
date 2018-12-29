# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:47:55 2018

@author: Emilio Gordon
"""

def ChannelInfoFunc (PATH_TO_IMAGE,subImage,class_name, absCoordX,absCoordY,im_width,im_height,xmin,ymin,xmax,ymax):
    # import the necessary packages
    from imutils import contours
    from skimage import measure
    import numpy as np
    import imutils
    import cv2
    import csv
    import os
    
    image = cv2.imread(PATH_TO_IMAGE)
    
    with open(os.path.join(os.getcwd(),'SubImages.csv'),'a',newline='') as csvfile:
        wrtr = csv.writer(csvfile, delimiter=',', quotechar='"')
        csvfile.flush() # whenever you want, and/or
    
        margin = 0
        
        # Get Channel Coordinates in px
        (left, right, top, bottom) = (ymin*im_width-margin, ymax*im_width+margin, xmin * im_height-margin, xmax * im_height+margin)
        
        # Look at just the channel
        image2 = image[absCoordX+int(top):absCoordX+int(bottom), int(left)+absCoordY:int(right)+absCoordY]
        #cv2.imshow("image2", image2)
        
        # Look at subImage
        #image3 = image[absCoordX:absCoordX+im_height, absCoordY:absCoordY+im_width]
        
        
        #Bounding Box Width and Height
        w = right-left
        h = bottom-top
        
        # Enclosing Circle
        cX = absCoordX+top+(h/2)
        cY = absCoordY+left+(w/2)
        radius = h//2
        
        
        wrtr.writerow([subImage,class_name,absCoordX,absCoordY,xmin,ymin,xmax,ymax, cX, cY])
        csvfile.flush()
    '''
        for (i, c) in enumerate(cnts):
            # draw the bright spot on the image
            (x, y, w, h) = cv2.boundingRect(c)
            ((cX, cY), radius) = cv2.minEnclosingCircle(c)
            cv2.circle(image, (int(cX), int(cY)), int(radius), (0, 0, 255), 3)
            cv2.rectangle(image, (x,y), (x+w,y+h), (0, 0, 255), 3)
            cv2.putText(image, "#{}".format(i + 1), (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            image2 = cv2.imread(os.path.join(path,str))
            image3 = image2[y:y+h,x:x+w]
            try:
                test = cv2.cvtColor(image3, cv2.COLOR_BGR2LAB)
                l_channel,a_channel,b_channel = cv2.split(test)
                lMean = np.mean(l_channel)
                
                gray2 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
                blurred2 = cv2.GaussianBlur(gray2, (11, 11), 0)
                thresh2 = cv2.threshold(blurred2, 10, 10, cv2.THRESH_BINARY)[1]
                thresh2 = cv2.erode(thresh2, None, iterations=2)
                thresh2 = cv2.dilate(thresh2, None, iterations=4)
                
                labels = measure.label(thresh2, neighbors=8, background=0)
                for label in np.unique(labels):
                    # if this is the background label, ignore it
                    if label == 0:
                        continue
                    labelMask2 = np.zeros(thresh2.shape, dtype="uint8")
                    labelMask2[labels == label] = 255
                    numPixels = cv2.countNonZero(labelMask2)
                
                #cv2.imshow("L_Channel",l_channel)
            except ValueError:
                numPixels = 1
                pass
                
            xRel = int(str[str.find('X')+1:str.find('Y')])
            yRel = int(str[str.find('Y')+1:str.find('P')])
            conv = 275 # Conversion 175px per 1mm     
            #NOTE: Due to camera rotation, the cY referes to placement of X and cX referes to placement of Y
            filewriter.writerow([str, int(cX)/conv, int(cY)/conv, int(radius)/conv, xRel - cY/conv, yRel + cX/conv, int(lMean), int(numPixels), int(w), int(h), int(w*h)])
'''