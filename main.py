import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import argparse

img = cv.imread('image.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred = cv.medianBlur(gray, 25) 
minDist = 100
param1 = 30 
param2 = 50 
minRadius = 5
maxRadius = 100 

circles = cv.HoughCircles(blurred, 
                           cv.HOUGH_GRADIENT, 
                           1,
                           minDist, 
                           param1=param1, 
                           param2=param2, 
                           minRadius=minRadius,
                           maxRadius=maxRadius)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)

ret,thresh = cv.threshold(blurred,127,255,0)

M = cv.moments(thresh)

cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])

cv.circle(img, (cX, cY), 5, (255, 255, 255), -1)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
