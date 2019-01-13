# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:01:46 2018

@author: Emilio Gordon

# Windows dependencies
# - Python 2.7.6: http://www.python.org/download/
# - OpenCV: http://opencv.org/
# - Numpy -- get numpy from here because the official builds don't support x64:
#   http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy

"""

import cv2
import numpy

cap = cv2.VideoCapture(0)
""
while(True):
    ret, frame = cap.read()    
    print(ret)
    if(ret == True):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

        cv2.imshow('frame', rgb)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            out = cv2.imwrite('capture.jpg', frame)
            break
""
cap.release()
cv2.destroyAllWindows()
