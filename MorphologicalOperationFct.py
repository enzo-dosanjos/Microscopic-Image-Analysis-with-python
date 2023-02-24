# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 00:09:37 2023

@author: Enzo
"""
import numpy as np


def erode(img, kernel, iteration):
    """
    verify for each pixel if every pixel around are white (for our chosen kernel). If it is the case, then the pixel
    is white else, the pixel is black. Hence, it extends the black color

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    kernel : array
        to verify for each pixel if every pixel around are white (for our chosen kernel).
    iteration : int
        nb of time we want to erode the image.

    Returns
    -------
    eroded_img : array
        array of the color values of the pixels in the eroded image.

    """
    img_row, img_col = img.shape
    kern_row, kern_col = kernel.shape
    eroded_img = img / 255  # to convert 255s into 1s

    new_row = img_row + kern_row - 1  # compute the row size of the new image with a padding
    new_col = img_col + kern_col - 1  # compute the column size of the new image with a padding
    new_image = np.zeros((new_row,
                          new_col))  # initialize an array of the size of the image with a padding of one pixel to
    # apply the kernel on every pixel of the image

    for it in range(iteration):
        for i in range(0, img_row):
            for j in range(0, img_col):  # to go through each pixel of the image
                new_image[i + 1, j + 1] = eroded_img[
                    i, j]  # give the pixel's color value of the image to create an identical image but, with a padding

        for i in range(0, img_row):
            for j in range(0, img_col):
                kernel_zone = new_image[i:i + kern_row,
                              j:j + kern_col]  # create a copy of a zone of pixels of the image of the same size as
                # the kernel
                if (
                        kernel_zone == kernel).all():  # verify for each pixel (each element of the array) in the
                    # kernel_zone if they are the same as the ones in the kernel
                    eroded_img[i, j] = 1  # if yes: the middle pixel of the kernel_zone is white
                else:
                    eroded_img[i, j] = 0  # if no: the middle pixel of the kernel_zone is black

    return eroded_img * 255  # to get it back to its normal pixel's color value


def dilate(img, kernel, iteration):
    """
    verify for each pixel if at least one pixel around is white (for our chosen kernel). If it is the case, then the pixel is white else, the pixel is black. Hence, it extend the white color

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    kernel : array
        to verify for each pixel if every pixel around are white (for our chosen kernel).
    iteration : int
        nb of time we want to dilate the image.

    Returns
    -------
    dilated_img : array
        array of the color values of the pixels in the dilated image.

    """
    img_row, img_col = img.shape
    kern_row, kern_col = kernel.shape
    dilated_img = img / 255  # to convert 255s into 1s

    new_row = img_row + kern_row - 1  # compute the row size of the new image with a padding
    new_col = img_col + kern_col - 1  # compute the column size of the new image with a padding
    new_image = np.zeros((new_row,
                          new_col))  # initialize an array of the size of the image with a padding of one pixel to
    # apply the kernel on every pixel of the image

    for it in range(iteration):
        for i in range(0, img_row):
            for j in range(0, img_col):  # to go through each pixel of the image
                new_image[i + 1, j + 1] = dilated_img[
                    i, j]  # give the pixel's color value of the image to create an identical image but, with a padding

        for i in range(0, img_row):
            for j in range(0, img_col):  # to go through each pixel of the image
                kernel_zone = new_image[i:i + kern_row,
                              j:j + kern_col]  # create a copy of a zone of pixels of the image of the same size as
                # the kernel
                if (
                        kernel_zone == kernel).any():  # verify if any of the pixels (any element of the array) in
                    # the kernel_zone is the same as the ones in the kernel
                    dilated_img[i, j] = 1  # if yes: the middle pixel of the kernel_zone is white
                else:
                    dilated_img[i, j] = 0  # if no: the middle pixel of the kernel_zone is black
    return dilated_img * 255  # to get it back to its normal pixel's color value
