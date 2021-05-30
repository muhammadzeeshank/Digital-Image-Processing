import numpy as np
import cv2


def thresholdByGlobalMean(image):
    img_mean = np.mean(image)
    threshed_img = cv2.threshold(image, img_mean, 255, cv2.THRESH_BINARY)[1]
    return threshed_img


def thresholdByGlobalMedian(image):
    img_median = np.median(image)
    threshed_img = cv2.threshold(image, img_median, 255, cv2.THRESH_BINARY)[1]
    return threshed_img


img = cv2.imread('images/img1.png', 0)
threshed_img1 = thresholdByGlobalMean(img)
threshed_img2 = thresholdByGlobalMedian(img)
cv2.imwrite('images/results/task1mean.jpg', threshed_img1)
cv2.imwrite('images/results/task1median.jpg', threshed_img2)
