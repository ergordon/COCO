# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 12:04:25 2019

@author: EPLab
"""
import os
import subprocess
from ChannelDetection import ChannelDetectionFunc

#subprocess.call(["activate","tensorflow"])

subprocess.run('activate tensorflow && "python coco.py" && source deactivate', shell=True)


