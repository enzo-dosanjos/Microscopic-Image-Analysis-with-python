# -*- coding: utf-8 -*-
"""
Created on Jan 28 13:07:00 2023

@author: Sacha
"""
import numpy as np


def flood(img, old_color, new_color):
    first_white = np.nonzero(img == old_color)

    while len(first_white[0]) > 0:

        img = fill2(img, first_white[0][0], first_white[1][0], old_color, new_color)
        first_white = np.nonzero(img == old_color)

    return img


def fill2(img, x, y, old_color, new_color):
    queued = [[x, y]]

    while len(queued) > 0:
        x = queued[0][0]
        y = queued[0][1]
        img[x][y] = new_color
        print(f' {x},{y} : set to {new_color}')
        queued.remove(queued[0])
        print(f"queue size {len(queued)} ")

        cellcheck = \
            [[x, y + 1],
             [x - 1, y], [x + 1, y],
             [x, y - 1]
             ]

        for elem in cellcheck:
            if img[elem[0]][elem[1]] == old_color and (elem not in queued):
                queued.append(elem)
                print(f' {elem} queued')

    return img
