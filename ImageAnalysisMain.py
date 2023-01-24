# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:45:05 2023

@author: Enzo
"""

import cv2
from ImageAnalysisFct import *
from skimage import io


img = cv2.imread("Metal_Structure.png", 0)


hist = histogram(img)
threshold = threshold(hist)
thresholded_img = get_thresholded_img(img, threshold)

cv2.imshow("thresholded image", thresholded_img) #to see the result
cv2.waitKey(0)