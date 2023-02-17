# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:45:05 2023

@author: Enzo && Sacha
"""

import cv2  # to install opencv: pip install opencv-python
import copy
from termcolor import colored  # to install termcolor: pip install termcolor
import os
import time
import PropertiesFct
from ThresholdFct import *
from MorphologicalOperationFct import *
from GaussianBlurFct import *
from FloodAlgo import *
from PropertiesFct import *

start = time.asctime()

start_calc = time.time()

currentpath = os.getcwd()  # get the current paths
picfold = os.path.join(currentpath, "Data")  # enter the "data folder" in the current path
datatxt = os.path.join(picfold, "Data.txt")

print("default picture name : \nMetal_Structure.png")

# img = cv2.imread("Metal_Structure.png", 0)

img = cv2.imread(str(input("Image name ? \n >")), 0)

print("yes this program is currently doing something.")

# cv2.imshow("original image", img)  # to see the original image


gaussian_kernel = np.array(
    [
        [1, 4, 7, 4, 1],
        [4, 16, 26, 16, 4],
        [7, 26, 41, 26, 7],
        [4, 16, 26, 16, 4],
        [1, 4, 7, 4, 1]
    ]
)

blured_img = blur(img, gaussian_kernel, 1)

cv2.imwrite(os.path.join(picfold, 'blured_img.png'),
            blured_img)  # save the image to the \Data folder, with the specific name

print("blurring" + colored(" done", "green"))

# cv2.imshow("blured image", blured_img)  # to see the result of blur


hist = histogram(img)
print("histogram" + colored(" plotted", "green"))

threshold = otsu_threshold(hist, img)
print(f"threshold of {threshold}" + colored(" found", "green"))

thresholded_img = thresholding(img, threshold)
print("thresholding" + colored(" done", "green"))

cv2.imwrite(os.path.join(picfold, 'thresholded.png'),
            thresholded_img)  # save the image to the \Data folder, with the specific name

# cv2.imshow("thresholded image", thresholded_img)  # to see the result of thresholding


kernel = np.ones((3, 3), np.uint8)  # kernel used by ImageJ
eroded_img = erode(thresholded_img, kernel, 3)
print("erosion" + colored(" done", "green"))

cv2.imwrite(os.path.join(picfold, '1steroded.png'), eroded_img)

# cv2.imshow("eroded image", eroded_img)  # to see the result of erosion

dilated_img = dilate(eroded_img, kernel, 2)
print("dilation" + colored(" done", "green"))

cv2.imwrite(os.path.join(picfold, 'dilated.png'),
            dilated_img)  # save the image to the \Data folder, with the specific name

cv2.imshow("dilated image", dilated_img)

flooded_img, nb_cells, color_list = floodrgb(dilated_img, [255, 255, 255])  # flood the img

cv2.imwrite(os.path.join(picfold, 'flooded.png'),
            flooded_img)  # save the image to the \Data folder, with the specific name

cv2.imshow("flooded", flooded_img)

# get the properties of each cell
pixels_to_m = 500e-9  # to define

cell_list = []

line_print = ["", f"{time.asctime()}", "", ""]

shapecount = [0, 0, 0, 0, 0]  # [triangle, square, circle, oblong, rectangle]


properties = get_props_with_dico(flooded_img, color_list)

for i, color in enumerate(color_list):
    area = properties[str(color) + "-area"]
    perimeter = properties[str(color) + "-perimeter"]
    height = properties[str(color) + "-max_height"]
    width = properties[str(color) + "-max_width"]
    
    shape = PropertiesFct.findshape(area, width, height, shapecount)  # find the shape of the cell
    
    cell_list.append([copy.deepcopy(area), copy.deepcopy(perimeter), copy.deepcopy(height), copy.deepcopy(width),
                      copy.deepcopy(shape)])  # save the data of each cell

    print(
        f"cell {i} : - Area : {area} pixels - Perimeter : {perimeter} pixels - Height : {height} pixels - Width : {width} pixels. Shape : {shape}."
    )
    line_print.append(
        f"cell {i} : - Area : {area} pixels - Perimeter : {perimeter} pixels - Height : {height} pixels - Width : {width} pixels. Shape : {shape}.")
    # add line to be printed in the text file bellow

print(
    f"Cell shape :  {shapecount[0]} triangle, {shapecount[1]} square, {shapecount[2]} cirlce, {shapecount[3]} oblong, {shapecount[4]} rectangle."
)

small, medium, big = regroup(cell_list)

line_print.append("")
line_print.append(f'small : {small} \n medium : {medium} \n big : {big}')

line_print.append('')
line_print.append(
    f"Cell shape :  {shapecount[0]} triangle, {shapecount[1]} square, {shapecount[2]} cirlce, {shapecount[3]} oblong, {shapecount[4]} rectangle.")

line_print.append("")
line_print.append(f"took {time.time() - start_calc}s to complete")

with open(datatxt, "w") as txt: # write data in a text file, in the \Data folder
    for line in line_print:
        txt.write(line)
        txt.write('\n')

print(f"end time : {time.asctime()}")

print(f"the program took {time.time() - start_calc} to complete")

cv2.waitKey(0) # allow the img to be shown

input("enter anything to close all window \n>")

cv2.destroyAllWindows()
