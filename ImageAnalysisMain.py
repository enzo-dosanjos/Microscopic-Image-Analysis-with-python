# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:45:05 2023

@author: Enzo && Sacha
"""

from termcolor import colored
import os
import time
import PropertiesFct
from ThresholdFct import *
from MorphologicalOperationFct import *
from GaussianBlurFct import *
from FloodAlgo import *
from PropertiesFct import *


def main():
    currentpath = os.getcwd()  # get the current paths
    picfold = os.path.join(currentpath, "Data")  # enter the "data folder" in the current path
    datatxt = os.path.join(picfold, "Data.txt")

    imgfold = os.path.join(currentpath, "Images")  # enter the "Images folder" in the current path

    print("default picture name : \nMetal_Structure.png")

    imagename = str(input("Image name ? (enter nothing to use the default picture)\n >"))
    if imagename == "":
        imagename = "Metal_Structure.png"
    img = cv2.imread(os.path.join(imgfold, imagename), 0)

    print("Currently running...")

    start_calc = time.time()

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

    hist = histogram(img)
    print("histogram" + colored(" plotted", "green"))

    threshold = otsu_threshold(hist, img)
    print(f"threshold of {threshold}" + colored(" found", "green"))

    thresholded_img = thresholding(img, threshold)
    print("thresholding" + colored(" done", "green"))

    cv2.imwrite(os.path.join(picfold, 'thresholded.png'),
                thresholded_img)  # save the image to the \Data folder, with the specific name

    kernel = np.ones((3, 3), np.uint8)  # kernel used by ImageJ
    eroded_img = erode(thresholded_img, kernel, 3)
    print("erosion" + colored(" done", "green"))

    cv2.imwrite(os.path.join(picfold, '1steroded.png'), eroded_img)

    dilated_img = dilate(eroded_img, kernel, 2)
    print("dilation" + colored(" done", "green"))

    cv2.imwrite(os.path.join(picfold, 'dilated.png'),
                dilated_img)  # save the image to the \Data folder, with the specific name

    cv2.imshow("dilated image", dilated_img)

    flooded_img, nb_cells, color_list = floodrgb(dilated_img, [255, 255, 255])  # flood the img

    cv2.imwrite(os.path.join(picfold, 'flooded.png'),
                flooded_img)  # save the image to the \Data folder, with the specific name

    cv2.imshow("flooded", flooded_img)

    cell_list = []

    line_print = ["", f"{time.asctime()}", "", ""]

    shapecount = [0, 0, 0, 0, 0]  # [triangle, square, circle, oblong, rectangle]

    properties = get_properties(flooded_img, color_list)

    for i, color in enumerate(color_list):
        area = properties[str(color) + "-area"]
        perimeter = properties[str(color) + "-perimeter"]
        height = properties[str(color) + "-max_height"]
        width = properties[str(color) + "-max_width"]

        shape = PropertiesFct.findshape(area, width, height, shapecount)  # find the shape of the cell

        cell_list.append(list([area, perimeter, height, width, shape]))  # save the data of
        # each cell

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

    with open(datatxt, "w") as txt:  # write data in a text file, in the \Data folder
        for line in line_print:
            txt.write(line)
            txt.write('\n')

    print(f"end time : {time.asctime()}")

    print(f"the program took {time.time() - start_calc} to complete")

    cv2.waitKey(10)  # allow the img to be shown

    input("enter anything to close all window \n>")

    cv2.destroyAllWindows()


main()
