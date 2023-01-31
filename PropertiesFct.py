# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:36:38 2023

@author: Enzo && Sacha
"""


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

            if list(img[i, j]) == colors and (
                    list(img[i - 1, j]) == [0, 0, 0] or list(img[i, j - 1]) == [0, 0, 0] or list(img[i + 1, j]) == [0,
                                                                                                                    0,
                                                                                                                    0] or list(
                    img[i, j + 1]) == [0, 0, 0]):
                perimeter_pixel_nb += 1

            if list(img[i, j]) == colors and list(img[i, j - 1]) != colors:
                while list(img[i, j]) == colors:
                    height += 1
                    j += 1
                if height > max_height:
                    max_height = height

            if list(img[i, j]) == colors and list(img[i - 1, j]) != colors:
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
            if list(img[i, j]) == colors and (
                    list(img[i - 1, j]) == [0, 0, 0] or list(img[i, j - 1]) == [0, 0, 0] or list(img[i + 1, j]) == [0,
                                                                                                                    0,
                                                                                                                    0] or list(
                    img[i, j + 1]) == [0, 0, 0]):
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
            if list(img[i, j]) == colors and list(img[i - 1, j]) != colors:
                while list(img[i, j]) == colors:
                    width += 1
                    i += 1
                if width > max_width:
                    max_width = width
    return max_width


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
