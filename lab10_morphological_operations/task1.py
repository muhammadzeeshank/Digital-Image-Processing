import numpy as np
import cv2
from numpy.lib.arraypad import pad
from functions import erosion

img = cv2.imread('images/erosion.jpg', 0)
# thresholding image
b_img = cv2.threshold(img, 127, 1, cv2.THRESH_BINARY)[1]
# structuring element
struct_element = np.ones((19, 19), np.uint8)
# applying erosion
final_img = erosion(b_img, struct_element)
cv2.imwrite('images/results/task1_img.jpg', final_img)
