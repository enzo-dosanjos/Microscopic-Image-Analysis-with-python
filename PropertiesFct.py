# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:36:38 2023

@author: Enzo
"""

import numpy as np

def get_properties(img, colors):
    """
    count the number of pixels in a cell, the number of pixels of the border of the cell and compute all the heights and widths in the cell

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    colors : list
        a list of the rgb colors of a cell.

    Returns
    -------
    area_pixel_nb : int
        the number of pixel in the cell.
    perimeter_pixel_nb : int
        the number of pixel of the border.
    max_height : int
        the highest height in the cell.
    max_width : int
        the highest width in the cell.

    """
    area_pixel_nb = 0
    perimeter_pixel_nb = 0
    max_height = 0
    max_width = 0
    
    img_row, img_col, rgb = img.shape
    
    for i in range(0, img_row):
        height = 0
        width = 0
        
        for j in range(0, img_col):
            if list(img[i, j]) == colors:
                area_pixel_nb += 1
                
            if list(img[i, j]) == colors and (list(img[i - 1, j]) == [0, 0, 0] or list(img[i, j - 1]) == [0, 0, 0] or list(img[i + 1, j]) == [0, 0, 0] or list(img[i, j + 1]) == [0, 0, 0]):
                perimeter_pixel_nb += 1
                
            if list(img[i, j]) == colors and list(img[i, j - 1]) != colors:
                while list(img[i, j]) == colors:
                    height += 1
                    j += 1
                if height > max_height:
                    max_height = height
                    
            if list(img[i, j]) == colors and list(img[i -1, j]) != colors:
                while list(img[i, j]) == colors:
                    width += 1
                    i += 1
                if width > max_width:
                    max_width = width
                    
    return area_pixel_nb, perimeter_pixel_nb, max_height, max_width


def get_area(img, colors):    
    """
    count the number of pixels in a cell (the number of pixels of the same color)

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    colors : list
        a list of the rgb colors of a cell.

    Returns
    -------
    area_pixel_nb : int
        the number of pixel in the cell.

    """
    img_row, img_col, rgb = img.shape
    
    area_pixel_nb = 0
    
    for i in range(0, img_row):
       for j in range(0, img_col):
            if list(img[i, j]) == colors:
                area_pixel_nb += 1
    return area_pixel_nb


def get_perimeter(img, colors):
    """
    count the number of pixels of the border of the cell (the number of pixels in a cell that have a black pixel next to it)

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    colors : list
        a list of the rgb colors of a cell.

    Returns
    -------
    perimeter_pixel_nb : int
        the number of pixel of the border.

    """
    img_row, img_col, rgb = img.shape
               
    perimeter_pixel_nb = 0
    
    for i in range(0, img_row):
       for j in range(0, img_col):
            if list(img[i, j]) == colors and (list(img[i - 1, j]) == [0, 0, 0] or list(img[i, j - 1]) == [0, 0, 0] or list(img[i + 1, j]) == [0, 0, 0] or list(img[i, j + 1]) == [0, 0, 0]):
                perimeter_pixel_nb += 1
    return perimeter_pixel_nb


def get_height(img, colors):
    """
    compute all the heights in the cell and return the highest

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    colors : list
        a list of the rgb colors of a cell.

    Returns
    -------
    max_height : int
        the highest height in the cell.

    """
    img_row, img_col, rgb = img.shape
               
    max_height = 0
    for i in range(0, img_row):
        height = 0
        for j in range(0, img_col):
            if list(img[i, j]) == colors and list(img[i, j - 1]) != colors:
                while list(img[i, j]) == colors:
                    height += 1
                    j += 1
                if height > max_height:
                    max_height = height
    return max_height


def get_width(img, colors):
    """
    compute all the widths in the cell and return the highest

    Parameters
    ----------
    img : array
        array of the color values of the pixels in the image.
    colors : list
        a list of the rgb colors of a cell.

    Returns
    -------
    max_width : int
        the highest width in the cell.

    """
    img_row, img_col, rgb = img.shape
               
    max_width = 0
    for i in range(0, img_row):
        width = 0
        for j in range(0, img_col):
            if list(img[i, j]) == colors and list(img[i -1, j]) != colors:
                while list(img[i, j]) == colors:
                    width += 1
                    i += 1
                if width > max_width:
                    max_width = width
    return max_width