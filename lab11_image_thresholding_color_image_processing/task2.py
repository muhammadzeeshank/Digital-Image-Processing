import numpy as np
import cv2

# thresholding by local mean
def thresholdByLocalMean(image):
    threshed_img = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 3)
    return threshed_img


# read image
img = cv2.imread('images/img1.png', 0)
threshed_img1 = thresholdByLocalMean(img)
# save image
cv2.imwrite('images/results/task2mean.jpg', threshed_img1)
