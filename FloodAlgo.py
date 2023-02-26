# -*- coding: utf-8 -*-
"""
Created on Jan 28 13:07:00 2023

@author: Sacha
"""
import numpy as np
import cv2
import random


def flood(img, old_color):
    """
    This flood the cells and fill them with different hue of gray

    Parameters
    ----------
    img : array - an image
    old_color : int - the old grayscale color you want replaced, int, [0-255]

    Returns
    -------
    img : array - the flooded image
    """
    first_white = np.nonzero(img == old_color)
    new_color = 0

    while len(first_white[0]) > 0:
        if new_color < 200:
            new_color += 20
        else:
            new_color = 20

        img = fill2(img, first_white[0][0], first_white[1][0], old_color, new_color)
        first_white = np.nonzero(img == old_color)

    return img


def floodrgb(img, old_color):
    """
    flood the cells with color
    Parameters
    ----------
    img : array - image before being flooded in grayscale or black and white
    old_color : list - the color that should be changed. format : [0-255, 0-255, 0-255]

    Returns
    -------
    img : array - the flooded image in rgb format
    cellcount : int - return the number of cell flooded
    color_list : list - list of all the used color
    """
    cellcount = 0

    img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    img = img.astype(np.uint8)

    first_white = np.nonzero(img == old_color)
    new_color = [10, 0, 0]

    color_list = []

    while len(first_white[0]) > 0:

        while new_color in color_list:
            new_color = [random.randint(20, 250), random.randint(1, 250), random.randint(1, 220)]

        color_list.append(list(new_color))

        # print(color_list)

        cellcount += 1  # this count the number of cell

        print(f"number of grains : {cellcount}")

        img = fill2(img, first_white[0][0], first_white[1][0], old_color, new_color)
        first_white = np.nonzero(img == old_color)

    return img, cellcount, color_list


def fill2(img, x, y, old_color, new_color):
    """
    sequential alogrithm that fill the cell with a color
    Parameters
    ----------
    img : array - the image to be filled
    x : int - x coordinate of the starting point
    y : int - y coordinate of the starting point
    old_color : list or int - the color that should be replaced. list if img is rgb, or int if img is grayscale
    new_color : list or int - the color that replace. list if img is rgb, int if img is grayscale

    Returns
    -------
    img : array - the image with the new filled cell

    """

    queued = [[x, y]]

    while len(queued) > 0:
        x = queued[0][0]
        y = queued[0][1]
        img[x][y] = new_color
        # print(f' {x},{y} : set to {new_color}')
        queued.remove(queued[0])
        # print(f"queue size {len(queued)} ")

        cellcheck = \
            [[x, y + 1],
             [x - 1, y], [x + 1, y],
             [x, y - 1]
             ]

        for elem in cellcheck:
            if img[elem[0]][elem[1]][0] == old_color[0] and img[elem[0]][elem[1]][1] == old_color[1] and \
                    img[elem[0]][elem[1]][2] == old_color[2] and (elem not in queued):
                queued.append(elem)
                # print(f' {elem} queued')

    return img
