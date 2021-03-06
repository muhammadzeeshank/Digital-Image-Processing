import numpy as np
import cv2
from numpy.lib.arraypad import pad
from functions import erosion

img = cv2.imread('images/erosion.jpg', 0)
# structuring element
struct_element = np.ones((19, 19), np.uint8)
# applying erosion
final_img = erosion(img, struct_element)
cv2.imwrite('images/results/task1_img.jpg', final_img)
