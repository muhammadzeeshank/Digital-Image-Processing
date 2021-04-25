import numpy as np
import cv2

img = cv2.imread("img2.jpg", 0)
imgv = img[::-1, :]
imgh = img[:, ::-1]
imgb = img[::-1, ::-1]
cv2.imshow('Original image', img)
cv2.imshow('Flipped horizontal image', imgh)
cv2.imshow('Flipped vertical image', imgv)
cv2.imshow('Flipped both image', imgb)


cv2.waitKey(0)
cv2.destroyAllWindows()
