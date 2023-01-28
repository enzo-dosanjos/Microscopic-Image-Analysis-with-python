# -*- coding: utf-8 -*-
"""
Created on Jan 28 13:07:00 2023

@author: Sacha
"""
import cv2
import FloodAlgo



img = cv2.imread("ClosedFloodTest.png", 0)

img = FloodAlgo.flood(img, 255, 128)

cv2.imshow("flooded", img)
print("ZZ")





cv2.waitKey(0)
