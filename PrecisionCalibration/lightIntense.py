# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:34:43 2018

@author: Emilio Gordon
"""  

def lightIntenseFunc (str, path):
    # import the necessary packages
    from imutils import contours
    from skimage import measure
    import numpy as np
    import imutils
    import cv2
    import csv
    import os
    
    image = cv2.imread(os.path.join(path,str))
    height, width, channels = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    
    # threshold the image to reveal light regions in the
    # blurred image
    #thresh = cv2.threshold(blurred, 100, 200, cv2.THRESH_BINARY)[1]
    thresh = cv2.threshold(blurred, 10, 10, cv2.THRESH_BINARY)[1]
    
    # perform a series of erosions and dilations to remove
    # any small blobs of noise from the thresholded image
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)
    
    # perform a connected component analysis on the thresholded
    # image, then initialize a mask to store only the "large"
    # components
    labels = measure.label(thresh, neighbors=8, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")
    
    holePixelCount = []
    
    # loop over the unique components
    for label in np.unique(labels):
        # if this is the background label, ignore it
        if label == 0:
            continue

        # otherwise, construct the label mask and count the
        # number of pixels 
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)
        
        # if the number of pixels in the component is sufficiently
        # large, then add it to our mask of "large blobs"
        if numPixels > 300:
            mask = cv2.add(mask, labelMask)
            holePixelCount.append(numPixels)

    # find the contours in the mask, then sort them from left to
    # right
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    try:
        cnts = contours.sort_contours(cnts)[0]
    except ValueError:
        pass

    # loop over the contours
    with open(os.path.join(path,'holes.csv'), mode='a') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|',quoting=csv.QUOTE_MINIMAL)
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
    
    #---------------#
    # NEW CODE HERE # 
    #---------------#
    newPath = path + "/ImageResults"
    cv2.imwrite(os.path.join(newPath , str), image)