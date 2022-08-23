# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 17:13:10 2022

@author: DevRehamMetwally
"""

import cv2
import numpy as np


img1 = cv2.imread("Downloads/puppy.jpg")
img1 = cv2.resize(img1,(1800,980))




img2 = cv2.imread("Downloads/opencv.png")
img2 = cv2.resize(img2,(400,400))


y_offset = img1.shape[0]-img2.shape[0]
x_offset = img1.shape[1]-img2.shape[1]

roi = img1[y_offset:img1.shape[0],x_offset:img1.shape[1]]

img2gray =cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)

mask_inv = cv2.bitwise_not(img2gray)

white_background = np.full(img2.shape,255,dtype=np.uint8)

background = cv2.bitwise_or(white_background,white_background,mask=mask_inv)

forground = cv2.bitwise_or(img2,img2,mask=mask_inv)

final_img = cv2.bitwise_or(roi,forground)

large_img = img1
small_img = final_img




large_img[y_offset:y_offset+img2.shape[0],x_offset:x_offset+img2.shape[1]] = small_img
cv2.imshow("final",large_img)