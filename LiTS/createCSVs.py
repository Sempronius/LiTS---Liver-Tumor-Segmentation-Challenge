#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 22:33:10 2019

@author: ryan
"""
import os
import csv

os.listdir(path='.')

'''
    For the given path, get the List of all files in the directory tree 
'''
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        #if os.path.isdir(fullPath):
        #    allFiles = allFiles + getListOfFiles(fullPath)
        #else:
        allFiles.append(fullPath)
                
    return allFiles

dirName = '/home/ryan/Documents/LiTS_data/Patch_Image_Mask/Image';
 
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)
listOfFiles.insert(0,'filename')

Image_csv = open("Image.csv",'w')

wr = csv.writer(Image_csv)

for item in listOfFiles:
    wr.writerow([item]) #add brackets, otherwise each character will have its own cell

dirName = '/home/ryan/Documents/LiTS_data/Patch_Image_Mask/MaskLiver';
 
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)
listOfFiles.insert(0,'filename')

Image_csv = open("MaskLiver.csv",'w')

wr = csv.writer(Image_csv)

for item in listOfFiles:
    wr.writerow([item]) #add brackets, otherwise each character will have its own cell
    
dirName = '/home/ryan/Documents/LiTS_data/Patch_Image_Mask/MaskTumor';
 
# Get the list of all files in directory tree at given path
listOfFiles = getListOfFiles(dirName)
listOfFiles.insert(0,'filename')

Image_csv = open("MaskTumor.csv",'w')

wr = csv.writer(Image_csv)

for item in listOfFiles:
    wr.writerow([item]) #add brackets, otherwise each character will have its own cell
    
#*******************************************************************************
    # CAN WE GET FIRST LINE TO BE FILENAME? "Filename" 
    # is that necessary?
    # Also, look at dataset_input.py 
    # What is the purpose of that? do I need to run it before VNET? 
    # go back and look at this guy's PROSTATE VNET. Maybe that makes more sense.?