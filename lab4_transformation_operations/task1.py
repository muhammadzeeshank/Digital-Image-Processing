import numpy as np
import cv2
import math
img = cv2.imread('square.tif', 0)
height, width = img.shape
maxofimg = np.max(img)
l = 255
c = 255/(math.log2(1 + maxofimg))
img1 = np.zeros([height, width], np.uint8)
img2 = np.zeros([height, width], np.uint8)
for x in range(width):
    for y in range(height):
        # For Negative Transformation
        img1[y][x] = l-img[y][x]
        # For Log Transformation
        img2[y][x] = c * (math.log2(img[y][x] + 1))

cv2.imshow('Negative Transformation', img1)
cv2.imshow('Log Transformation', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
