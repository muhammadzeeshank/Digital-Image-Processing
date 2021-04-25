import cv2
import numpy as np

img = cv2.imread('img0.png')
height, width, _ = img.shape
paddwidth = round(width * 10/100)
newidth = width + paddwidth
paddhieght = round((newidth - height)/2)
paddedimg = cv2.copyMakeBorder(img, paddhieght, paddhieght, paddwidth,
                               paddwidth, cv2.BORDER_CONSTANT, 0)
cv2.imshow('image', paddedimg)
print(paddedimg.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()
