# -*- coding: utf-8 -*-
"""
Created on Jan 28 13:07:00 2023

@author: Sacha
"""
import cv2
import FloodAlgo

img = cv2.imread("FloodTest2.png", 0)



img = FloodAlgo.floodrgb(img, [255, 255, 255])
for i in range(1, len(img)):
    print(img[i])


cv2.imshow("flooded", img[0])
print("ZZ")





cv2.waitKey(0)
