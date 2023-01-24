# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:45:06 2023

@author: Enzo
"""

import matplotlib.pyplot as plt
import numpy as np


#Threshold
def histogram(img):
    """
    make an histogram with the number of appearance of each color values in the pixels of the image

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.

    Returns
    -------
    nb_appearance : array
        array with the number of appearance of each color values.

    """
    row, col = img.shape #get the number of rows and colons of pixels of the image
    nb_appearance = np.zeros(256) #create an array of zeros to initialize nb_appearance
    for i in range(0,row):
       for j in range(0,col): #go through each pixel of the image
          nb_appearance[img[i,j]] += 1 #make the histogram by increasing by 1 each time a value between 0 to 255 appear for each pixel of the image because the grey pixels appear more often than black pixels
    return nb_appearance


def threshold(hist):
    """
    determine automatically the threshold between black or white pixels

    Parameters
    ----------
    hist : array
        histogram with the number of appearance of each color values in the pixels of the image.

    Returns
    -------
    threshold : int
        threshold between black or white pixels.

    """
    median = np.median(hist) #compute the median of the histogram dataset
    i = 0
    while hist[i] < median * 1.2:
        i+= 1
    threshold = i
    return threshold


def get_thresholded_img(img, threshold):
    """
    transform, according to the threshold value, each pixel's color value to white or black 

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    threshold : int
        threshold between black or white pixels.

    Returns
    -------
    new_img : array
        array of the pixel's color value transformed to either black or white.

    """
    row, col = img.shape 
    new_img = np.zeros((row, col)) #make an array of the same size as the image
    for i in range(0,row):
        for j in range(0,col):
            if img[i,j] >= threshold: #verify if the color value of the pixel is higher than the threshold
                new_img[i,j] = 255 #if yes : transform to a white pixel
            else:
                new_img[i,j] = 0 #if no : transform to a black pixel
    return new_img