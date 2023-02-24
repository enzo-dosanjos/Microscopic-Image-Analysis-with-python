# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:36:38 2023

@author: Enzo && Sacha
"""

import cv2


def get_properties(img, list_colors):
    properties = {"[0, 0, 0]-area": 0, "[0, 0, 0]-perimeter": 0, "[0, 0, 0]-last_height": 0, "[0, 0, 0]-max_height": 0,
                  "[0, 0, 0]-last_width": 0, "[0, 0, 0]-max_width": 0}

    img_row, img_col, rgb = img.shape

    for color in list_colors:
        properties[str(color) + "-area"] = 0
        properties[str(color) + "-perimeter"] = 0
        properties[str(color) + "-max_height"] = 0
        properties[str(color) + "-last_height"] = 0
        properties[str(color) + "-max_width"] = 0
        properties[str(color) + "-last_width"] = 0

    for i in range(img_row):

        # for the height
        for key in properties.keys():
            if key.endswith("-last_height"):
                properties[key] = 0

        for j in range(img_col):
            # get area
            properties[str(list(img[i, j])) + "-area"] += 1

            # get border
            if list(img[i - 1, j]) == [0, 0, 0] or list(img[i, j - 1]) == [0, 0, 0] or list(img[i + 1, j]) == [0, 0,
                                                                                                               0] or list(
                    img[i, j + 1]) == [0, 0, 0]:
                properties[str(list(img[i, j])) + "-perimeter"] += 1

            # get height
            properties[str(list(img[i, j])) + "-last_height"] += 1
            if properties[str(list(img[i, j])) + "-last_height"] > properties[str(list(img[i, j])) + "-max_height"]:
                properties[str(list(img[i, j])) + "-max_height"] = properties[str(list(img[i, j])) + "-last_height"]

    # get width
    for j in range(img_col):
        for key in properties.keys():
            if key.endswith("-last_width"):
                properties[key] = 0
        for i in range(img_row):
            properties[str(list(img[i, j])) + "-last_width"] += 1
            if properties[str(list(img[i, j])) + "-last_width"] > properties[str(list(img[i, j])) + "-max_width"]:
                properties[str(list(img[i, j])) + "-max_width"] = properties[str(list(img[i, j])) + "-last_width"]

    # delete useless dictionary keys
    to_del = []
    for key in properties.keys():
        if key.endswith("-last_height") or key.endswith("-last_width"):
            to_del.append(key)
    for k in to_del:
        properties.pop(k, None)

    return properties


def findshape(area, width, height, shapecount):
    """
    Tries to find the closest form of each cell
    Parameters
    ----------
    area : int - area of the cell
    width : int - width of the cell
    height : int - height of the cell
    shapecount : list of int - format : [triangle, square, circle, oblong, rectangle]

    Returns
    -------
    shapelistname[i] : str - name of the shape
    shapecount : list of int - format : [triangle, square, circle, oblong, rectangle]
    """
    triangle = abs((0.5 * width * height) - area)
    square = abs((width * width) - area)
    circle = abs(((width / 2) * 3.14 ** 2) - area)
    oblong = abs((3.14 * (width / 2) * (height / 2)) - area)
    rectangle = abs((width * height) - area)

    shapelist = [triangle, square, circle, oblong, rectangle]
    shapelistname = ["triangle", "square", "circle", "oblong", "rectangle"]
    correct = min(shapelist)

    for i in range(len(shapelist)):
        if shapelist[i] == correct:
            shapecount[i] = shapecount[i] + 1
            return shapelistname[i], shapecount


def regroup(cell_list):
    """
    group the cell in 3 categories :
    small, medium, big

    Parameters
    ----------
    cell_list : list of int - list of cells and their caracteristic. format : [area, ...]

    Returns
    -------
    small : list - all the small cell along with caracteristics
    medium : list - all the medium cell along with caracteristics
    big : list - all the big cell along with caracteristics

    """
    small = []
    medium = []
    big = []

    for i in range(len(cell_list)):
        if cell_list[i][0] < 250:
            small.append(cell_list[i])
        elif 250 <= cell_list[i][0] < 600:
            medium.append(cell_list[i])
        else:
            big.append(cell_list[i])
    return small, medium, big
