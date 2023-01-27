# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:18:10 2023

@author: Enzo
"""

import numpy as np


def blur(img, kernel, iteration):
    """
    compute for each pixel the average of the pixel's color value around with a certain weight for each neighboring pixels depending on the defined kernel (simple: blur the image)

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    kernel : array
        to verify for each pixel if every pixels around are white (for our chosen kernel).
    kern_size : int
        sum of the pixel's weight given by the kernel.
    iteration : int
        nb of time we want to blur the image.

    Returns
    -------
    blured_img : array
        array of the color values of the pixels in the blured image.

    """
    img_row, img_col = img.shape
    kern_row, kern_col = kernel.shape
    blured_img = img
    
    new_row = img_row + kern_row -1 #compute the row size of the new image with a padding
    new_col = img_col + kern_col -1 #compute the column size of the new image with a padding
    new_image = np.zeros((new_row, new_col)) #initialize an array of the size of the image with a padding of one pixel to apply the kernel on every pixels of the image
    
    for it in range(iteration):
        for i in range(0, img_row):
           for j in range(0, img_col):  #to go through each pixels of the image
               new_image[i+1, j+1] = blured_img[i, j] #give the pixel's color value of the image to create a identical image but, with a padding
               
        for i in range(0, img_row):
           for j in range(0, img_col):
               kernel_zone = new_image[i:i+kern_row, j:j+kern_col] #create a copy of a zone of pixels of the image of the same size as the kernel
               blured_pxl_val = 0
               for k in range(0, kern_row):
                  for l in range(0, kern_col):  #to go through each pixels of the kernel_zone
                      blured_pxl_val += (kernel_zone[k, l] * kernel[k , l])/np.sum(kernel) #compute the mean of the pixel's color value arround a pixel with a certain weight for each pixel determined by the kernel
               blured_img[i, j] = blured_pxl_val
    return blured_img