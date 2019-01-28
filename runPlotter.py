# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:31:31 2019

@author: EPLab
"""

import csv
from PlotHoles import PlotHolesFunc
import argparse
import os

filename = input("Enter Test Name: ")
path = "C:/Users/EPLab/Desktop/COCO/"+filename

PlotHolesFunc (path)
