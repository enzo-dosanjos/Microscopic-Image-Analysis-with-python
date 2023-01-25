# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:44:49 2023

@author: Enzo
"""
# to install opencv: pip install opencv-python
import cv2 #to read and clean the image
import numpy as np #to create array
import matplotlib.pyplot as plt #to plot the threshold
import pandas as pd #to analyse the grain properties
from scipy import ndimage #to label the grains
from skimage import io, color, measure

#Read image
img = cv2.imread("Metal_Structure.png", 0) #read the microscopic image and convert it to a matrix(the "0" is to convert in greyscale)
pixels_to_m = 500e-9 #to define


#clean image
blured_image = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("blured image", blured_image)

#plt.hist(img.flat, bins = 100, range=(0,255)) #to determine the threshold value manually
img_return, img_thresholded = cv2.threshold(blured_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) #return the recommanded threshold for the image and put the value 255 (black) to the pixels corresponding to the grains border and 0 (white) for the others
print(img_return)

kernel = np.ones((3, 3), np.uint8)
#np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])+
img_eroded = cv2.erode(img_thresholded, kernel, iterations=2) #to fill the holes between the grains border created with the threshold
img_dilated = cv2.dilate(img_eroded, kernel, iterations=2) #then dilate to get the borders back to their original size


#cv2.imshow("eroded image", img_eroded)
#cv2.imshow("Thresholded Image", img_thresholded)
#cv2.imshow("Dilated Image", img_dilated) #to test the result of thresholding, erosion and dilate
cv2.waitKey(0)


#create mask
mask = img_dilated == 255 #get the border of the grains by taking every pixels = to 255
#io.imshow(mask) #to verify the result of the mask


#label the grains
labeled_mask, nb_labels = ndimage.label(mask, structure = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]) #the structure determine when a pixel is linked to another (the one that I put is the one used by ImageJ)

#img_labelled = color.label2rgb(labeled_mask, bg_label = 0)
#cv2.imshow("colored label image", img_labelled) #to verify the result of the labeled mask
#cv2.waitKey(0)

"""
#measure the properties of each grains
clusters = measure.regionprops(labeled_mask, img) #properties: Area, Orientation, Perimeter, Major/MinorAxisLenght
for properties in clusters:
    print(f"label : {properties.label} Area : {properties.area} Perimeter : {properties.perimeter}")
"""