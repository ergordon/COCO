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
START_TIME = time.time()

TensorflowPath = 'C:/ObjectDetection/models/research/object_detection'
sys.path.append(TensorflowPath)

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'inference_graph'
IMAGE_NAME = "test3.jpg"

# Path to frozen detection graph .pb file, which contains the model that is used
# for object detection.
PATH_TO_CKPT = 'C:/ObjectDetection/models/research/object_detection/inference_graph/frozen_inference_graph.pb'

# Path to label map file
PATH_TO_LABELS = 'C:/ObjectDetection/models/research/object_detection/data/object-detection.pbtxt'

# Path to image
#PATH_TO_IMAGE = 'C:/ObjectDetection/models/research/object_detection/'+IMAGE_NAME
# Path to image -- Grab path to current working directory
PATH_TO_IMAGE = 'C:/Users/EPLab/Desktop/COCO/BIPP/'+IMAGE_NAME

# Number of classes the object detector can identify
NUM_CLASSES = 4

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

# Define input and output tensors (i.e. data) for the object detection classifier

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

# Load image using OpenCV and
# expand image dimensions to have shape: [1, None, None, 3]
# i.e. a single-column array, where each item in the column has the pixel RGB value
image = cv2.imread(PATH_TO_IMAGE)
image_expanded = np.expand_dims(image, axis=0)

# Perform the actual detection by running the model with the image as input
(boxes, scores, classes, num) = sess.run(
    [detection_boxes, detection_scores, detection_classes, num_detections],
    feed_dict={image_tensor: image_expanded})

# Draw the results of the detection (aka 'visulaize the results')
vis_util.visualize_boxes_and_labels_on_image_array(
    image,
    np.squeeze(boxes),
    np.squeeze(classes).astype(np.int32),
    np.squeeze(scores),
    category_index,
    use_normalized_coordinates=True,
    line_thickness=2,
    min_score_thresh=0.50)

### CWH: Print the object details to the console instead of visualizing them with the code above
classes = np.squeeze(classes).astype(np.int32)
scores = np.squeeze(scores)
boxes = np.squeeze(boxes)
 
threshold = 0.50  #CWH: set a minimum score threshold of 50%
obj_above_thresh = sum(n > threshold for n in scores)
print("detected %s objects in %s above a %s score" % ( obj_above_thresh, PATH_TO_IMAGE, threshold))
 
for c in range(0, len(classes)):
  if scores[c] > threshold:
      class_name = category_index[classes[c]]['name']
      print(" object %s is a %s - score: %s, location: %s" % (c, class_name, scores[c], boxes[c]))


print("Elapsed Time: "+ str(time.time() - START_TIME) + " sec" )
