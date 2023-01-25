# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:45:05 2023

@author: Enzo
"""

import cv2 #to install opencv: pip install opencv-python
from termcolor import colored #to install termcolor: pip install termcolor
from ThresholdFct import *
from MorphologicalOperationFct import *


img = cv2.imread("Metal_Structure.png", 0)


hist = histogram(img)
threshold = threshold(hist)
thresholded_img = get_thresholded_img(img, threshold)
print("thresholding" + colored(" done", "green"))

#cv2.imshow("thresholded image", thresholded_img) #to see the result of thresholding


kernel = np.ones((3, 3), np.uint8) #kernel used by ImageJ
eroded_img = erode(thresholded_img, kernel, 2)
print("erosion" + colored(" done", "green"))

dilated_img = dilate(eroded_img, kernel, 2)
print("dilation" + colored(" done", "green"))

#cv2.imshow("eroded image", eroded_img) #to see the result of erosion
cv2.imshow("dilated image", dilated_img) #to see the result of dilation
cv2.waitKey(0)