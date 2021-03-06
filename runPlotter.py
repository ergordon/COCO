# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:31:31 2019

@author: Emilio Gordon
"""

from PlotHoles import PlotHolesFunc
from ComparePlots import ComparePlotsFunc
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("--compare", type=bool, default=False, required=False,
	help="compare == True if you want to compare tests")
ap.add_argument("--range", type=bool, default=False, required=False,
   help="range == True if you want to limit the plotting range")
args = vars(ap.parse_args())

if (args["compare"] == False):
    filename = input("Enter Test Name: ")
    path = "C:/Users/EPLab/Desktop/COCO/"+filename
    PlotHolesFunc (path, args["range"])
else:
    path = "C:/Users/EPLab/Desktop/COCO/"
    filenameA = input("Enter the First Test Name: ")
    filenameB = input("Enter the Second Test Name: ")
    ComparePlotsFunc (path, filenameA, filenameB, args["range"])
