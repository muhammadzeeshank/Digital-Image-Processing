import numpy as np
import cv2
img = cv2.imread('tungsten.tif', 0)
height, width = img.shape
img1 = np.zeros([height, width], np.uint8)
for x in range(width):
    for y in range(height):
        if img[y][x] >= 100 and img[y][x] <= 200:
            img1[y][x] = 210

cv2.imshow('Sliced image', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
