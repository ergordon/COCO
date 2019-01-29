# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 10:31:31 2019

@author: EPLab
"""

import csv
from PlotHoles import PlotHolesFunc
from ComparePlots import ComparePlotsFunc
import argparse
import os

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--compare", type=bool, default=False, required=False,
	help="Compare == True if you want to compare tests")
args = vars(ap.parse_args())


if (args["compare"] == False):
    filename = input("Enter Test Name: ")
    path = "C:/Users/EPLab/Desktop/COCO/"+filename
    PlotHolesFunc (path)
else:
    path = "C:/Users/EPLab/Desktop/COCO/"
    filenameA = input("Enter the First Test Name: ")
    filenameB = input("Enter the Second Test Name: ")
    ComparePlotsFunc (path, filenameA, filenameB)
