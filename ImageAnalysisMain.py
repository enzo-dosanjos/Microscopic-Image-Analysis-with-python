# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:45:05 2023

@author: Enzo
"""

import cv2 #to install opencv: pip install opencv-python
from termcolor import colored #to install termcolor: pip install termcolor
from ThresholdFct import *
from MorphologicalOperationFct import *
from GaussianBlurFct import *


img = cv2.imread("sudoku.jpg", 0)

#cv2.imshow("original image", img) #to see the original image


gaussian_kernel = np.array([[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4], [1, 4, 7, 4, 1]])
blured_img = blur(img, gaussian_kernel, 1)
print("bluring" + colored(" done", "green"))

#cv2.imshow("blured image", blured_img) #to see the result of blur


hist = histogram(img)
print("histogram" + colored(" plotted", "green"))

threshold = otsu_threshold(hist, img)
print("threshold" + colored(" found", "green"))

thresholded_img = thresholding(img, threshold)
print("thresholding" + colored(" done", "green"))

cv2.imshow("thresholded image", thresholded_img) #to see the result of thresholding


kernel = np.ones((3, 3), np.uint8) #kernel used by ImageJ
eroded_img = erode(thresholded_img, kernel, 2)
print("erosion" + colored(" done", "green"))

cv2.imshow("eroded image", eroded_img) #to see the result of erosion


dilated_img = dilate(eroded_img, kernel, 2)
print("dilation" + colored(" done", "green"))

cv2.imshow("dilated image", dilated_img) #to see the result of dilation
cv2.waitKey(0)