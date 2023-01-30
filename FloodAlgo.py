# -*- coding: utf-8 -*-
"""
Created on Jan 28 13:07:00 2023

@author: Sacha
"""
import numpy as np
import cv2
import copy
import random


def flood(img, old_color):
    """
    This flood the cells and fill them with differents hue of gray

    Parameters
    ----------
    img : an image
    old_color : the old grayscale color you want replaced, int, [0-255]

    Returns
    -------
    img : the flooded image
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
    flood the cells
    Parameters
    ----------
    img : the image, 2d array
    old_color : the color to change, list[int]

    Returns
    -------
    img : the flooded img, 2d array
    cellcount : the number of cell flooded, int
    color_list : list of all the colored cells
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

        color_list.append(copy.deepcopy(new_color))

        print(color_list)

        cellcount += 1      # this count the number of cell

        print(cellcount)

        img = fill2(img, first_white[0][0], first_white[1][0], old_color, new_color)
        first_white = np.nonzero(img == old_color)

    return img, cellcount, color_list


def fill2(img, x, y, old_color, new_color):

    queued = [[x, y]]

    while len(queued) > 0:
        x = queued[0][0]
        y = queued[0][1]
        img[x][y] = new_color
        #print(f' {x},{y} : set to {new_color}')
        queued.remove(queued[0])
        #print(f"queue size {len(queued)} ")

        cellcheck = \
            [       [x, y + 1],
             [x - 1, y], [x + 1, y],
                   [x, y - 1]
             ]

        for elem in cellcheck:
            if img[elem[0]][elem[1]][0] == old_color[0] and img[elem[0]][elem[1]][1] == old_color[1] and \
                    img[elem[0]][elem[1]][2] == old_color[2] and (elem not in queued):
                queued.append(elem)
                #print(f' {elem} queued')

    return img

