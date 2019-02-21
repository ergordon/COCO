# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 12:23:39 2019

@author: EPLab
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:08:43 2019

@author: EPLab
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 14:46:00 2018

@author: Emilio Gordon
"""

# Import packages
import os
import cv2
import numpy as np
import tensorflow as tf
import sys
import time
import imutils
import csv
from ChannelInfo2 import ChannelInfoFunc

filename = input("Enter the test name you would like to detect channels for: \n ")
print("Must be the same as the tested array length. (Note: Can be fixed later if input was incorrect)")
ARRlength = input("Enter Array Length [cm] (X-axis): ")
ARRwidth = input("Enter Array Width [cm] (Y-axis): ")

#Begin Timer
START_TIME = time.time()

raw_path = os.getcwd()
path = raw_path+"/"+str(filename)

TensorflowPath = 'C:/ObjectDetection/models/research/object_detection'
sys.path.append(TensorflowPath)

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'inference_graph'
IMAGE_NAME = "Stitched.jpg"

# Path to frozen detection graph .pb file, which contains the model that is used for object detection.
PATH_TO_CKPT = 'C:/ObjectDetection/models/research/object_detection/inference_graph/frozen_inference_graph.pb'

# Path to label map file
PATH_TO_LABELS = 'C:/ObjectDetection/models/research/object_detection/data/object-detection.pbtxt'

# Path to image
PATH_TO_IMAGE = path+"/"+IMAGE_NAME

PATH_TO_OUTPUT = path + "/Detections"
try:  
    os.mkdir(PATH_TO_OUTPUT)
    os.mkdir(path + "/Channels")
    os.mkdir(path + "/Channels/Light")
    os.mkdir(path + "/Channels/Grey")
    os.mkdir(path + "/Channels/Dark")
except OSError:  
    print ("Creation of the directory %s failed" % PATH_TO_OUTPUT)
else:  
    print ("Successfully created the directory %s" % PATH_TO_OUTPUT)
    
# Number of classes the object detector can identify
NUM_CLASSES = 1

# Load the label map.
# Label maps map indices to category names
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

## Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

# Get the image and its dimensions
print(PATH_TO_IMAGE)
image = cv2.imread(PATH_TO_IMAGE)
image = cv2.flip(image, 0) # Perform a verticle flip so that the original image and plots match.
height, width, channels = image.shape

## Array Width and Height in mm
arrayWidth = float(ARRlength)*10
arrayHeight = float(ARRwidth)*10

convX = arrayWidth/height
convY = arrayHeight/width


print(convX, convY)

## Make the subdivisions
maxImgWidth = 850
maxImgHeight = 500

divideWidth = 2
divideHeight = 2

N = width//divideWidth
M = height//divideHeight
 
while M >= maxImgHeight:
    divideHeight = divideHeight + 1
    M = height//divideHeight

while N >= maxImgWidth:
    divideWidth = divideWidth + 1
    N = width//divideWidth
    
print("\nThe input image is "+str(height)+"px by "+str(width)+" px")
print("This image will be divided into %s by %s sub-images for a total of %s images." % (divideHeight, divideWidth, divideHeight*divideWidth))  
print("Each sub-image will be "+str(M)+"px by "+str(N)+" px \n")

with open(os.path.join(path,'Channels.csv'),'w') as csvfile:
    wrtr = csv.writer(csvfile, delimiter=',', quotechar='"')
    wrtr.writerow(["SubImage Number","Class Name","RelativeOriginX2Absolute","RelativeOriginY2Absolute","Ymin","Xmin","Ymax","Xmax","pxcX","pxcY","cmcX","cmcY", "luminance", "width", "height"])
    csvfile.flush()

tiles = []
for x in range(0,height,M):
    for y in range(0,width,N):
        #tiles.append(image[x:x+M,y:y+N]) 
        tiles.append(1)
        PIC_TIME = time.time()
        
        print('Now processing subImage '+str(len(tiles)))
        
        tile = image[x:x+M+0,y:y+N+0]
        tile_expanded = np.expand_dims(tile, axis=0)
                   
        # Perform the actual detection by running the model with the image as input
        (boxes, scores, classes, num) = sess.run([detection_boxes, detection_scores, detection_classes, num_detections],feed_dict={image_tensor: tile_expanded})
        
        # Draw the results of the detection (aka 'visulaize the results')
        vis_util.visualize_boxes_and_labels_on_image_array(
            tile,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=2,
            min_score_thresh=0.50,
            max_boxes_to_draw=None,
            skip_scores=False,
            skip_labels=True)
        
        cv2.imwrite(os.path.join(PATH_TO_OUTPUT,'detection'+str(len(tiles))+'.jpg'), tile)
        
        classes = np.squeeze(classes).astype(np.int32)
        scores = np.squeeze(scores)
        boxes = np.squeeze(boxes)
        threshold = 0.50  #CWH: set a minimum score threshold of 50%
        obj_above_thresh = sum(n > threshold for n in scores)
        print("Detected %s Channels" % (obj_above_thresh))
        
        for c in range(0, len(classes)):
            if scores[c] > threshold:
                class_name = category_index[classes[c]]['name']
                ChannelInfoFunc (path,PATH_TO_IMAGE,"subImage_"+str(len(tiles)),str(class_name),int(x),int(y),N,M,boxes[c,0], boxes[c,1], boxes[c,2], boxes[c,3], convX, convY, c)

        print("Image Processing Time Elapsed Time: "+ str(time.time() - PIC_TIME) + " sec \n" )

print("Total Elapsed Time: "+ str(time.time() - START_TIME) + " sec" )
