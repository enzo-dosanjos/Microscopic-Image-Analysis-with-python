# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:45:06 2023

@author: Enzo
"""

import matplotlib.pyplot as plt
import numpy as np


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
    row, col = img.shape  # get the number of rows and colons of pixels of the image
    nb_appearance = np.zeros(256)  # create an array of zeros to initialize nb_appearance
    for i in range(0, row):
        for j in range(0, col):  # go through each pixel of the image
            nb_appearance[img[
                i, j]] += 1  # make the histogram by increasing by 1 each time a value between 0 to 255 appear for each pixel of the image because the grey pixels appear more often than black pixels
    plt.plot(nb_appearance)
    plt.show()
    return nb_appearance


def otsu_threshold(hist, img):
    """
    determine automatically the threshold between black or white pixels with otsu's method'

    Parameters
    ----------
    hist : array
        histogram with the number of appearance of each color values in the pixels of the image.
    img : array
        array of the color values of the pixels in the image.

    Returns
    -------
    i_min : int
        threshold between black or white pixels : indice for which the sum of the foreground and background spread is minimum

    """
    nb_pixels = float(np.product(img.shape))  # nb of pixels in the image
    # initializations
    i_min = 0
    min_within_class_var = 10000000
    threshold_try = 1

    while threshold_try < 256 and (
            threshold_try < 50 or i_min != threshold_try - 3):  # prevent to try threshold beyond 255 and stop when the indice of the minimum variation is found
        # new_img = thresholding(img, threshold_try)

        background = hist[
                     :threshold_try]  # the pixels that should be black according to the threshold that is being tried (below the threshold)
        foreground = hist[
                     threshold_try:]  # the pixels that should be white according to the threshold that is being tried (above the threshold)

        # computing weights
        w_background = np.sum(
            background) / nb_pixels  # compute the weight of every pixel's color value below the threshold which is being tried
        w_foreground = np.sum(
            foreground) / nb_pixels  # compute the weight of every pixel's color value above the threshold which is being tried

        # computing mean
        mean_background = np.sum(
            [pixel_value * nb_appearance for pixel_value, nb_appearance in enumerate(background)]) / np.sum(
            background)  # compute the mean of every pixel's color value below the threshold which is being tried multiplied by their number of appearance
        mean_foreground = np.sum(
            [pixel_value * nb_appearance for pixel_value, nb_appearance in enumerate(foreground)]) / np.sum(
            foreground)  # compute the mean of every pixel's color value below the threshold which is being tried multiplied by their number of appearance

        # computing variance
        var_background = np.nan_to_num(np.sum(
            [(pixel_value - mean_background) ** 2 * nb_appearance for pixel_value, nb_appearance in
             enumerate(background)]) / np.sum(background))  # compute the variance of the background
        var_foreground = np.nan_to_num(np.sum(
            [(pixel_value - mean_foreground) ** 2 * nb_appearance for pixel_value, nb_appearance in
             enumerate(foreground)]) / np.sum(foreground))  # compute the variance of the foreground
        # convert np.nan_to_num convert the result nan (that we don't want) to a number, usually 0

        # compute within class variance
        within_class_var = w_background * var_background + w_foreground * var_foreground  # compute the sum of the foreground and background spread

        # get the indice for which the sum of the foreground and background spread is minimum
        if within_class_var < min_within_class_var:
            i_min = threshold_try - 1
            min_within_class_var = within_class_var
        print(f"trying : {threshold_try - 1}")
        threshold_try += 1
    return i_min


def thresholding(img, threshold):
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
    new_img = np.zeros((row, col))  # make an array of the same size as the image
    for i in range(0, row):
        for j in range(0, col):
            if img[i, j] >= threshold:  # verify if the color value of the pixel is higher than the threshold
                new_img[i, j] = 255  # if yes : transform to a white pixel
            else:
                new_img[i, j] = 0  # if no : transform to a black pixel
    return new_img
