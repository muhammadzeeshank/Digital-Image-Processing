import numpy as np
import cv2
import math
img = cv2.imread('square.tif', 0)
height, width = img.shape
img1 = np.zeros([height, width], np.uint8)
meanofimg = int(np.mean(img))
for x in range(width):
    for y in range(height):
        if img[y][x] < meanofimg:
            img[y][x] = 0
        elif img[y][x] > meanofimg:
            img[y][x] = 255

for x in range(width):
    for y in range(height):
        if img[y][x] > meanofimg:
            img1[y][x] = 0
        elif img[y][x] < meanofimg:
            img1[y][x] = 255
cv2.imshow('L-0 G-255', img)
cv2.imshow('L-255 G-0', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
