import numpy as np
import cv2
img = cv2.imread('square.tif', 0)
height, width = img.shape
gamma = [0.2, 0.5, 1.2, 1.8]
img1 = np.zeros([height, width])
img2 = np.zeros([height, width])
img3 = np.zeros([height, width])
img4 = np.zeros([height, width])
for x in range(width):
    for y in range(height):
        img1[y][x] = 255 * ((img[y][x]/255)**gamma[0])
        img2[y][x] = 255 * ((img[y][x]/255)**gamma[1])
        img3[y][x] = 255 * ((img[y][x]/255)**gamma[2])
        img4[y][x] = 255 * ((img[y][x]/255)**gamma[3])

cv2.imshow('PLT 0.2', img1)
cv2.imshow('PLT 0.5', img2)
cv2.imshow('PLT 1.2', img3)
cv2.imshow('PLT 1.8', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()
