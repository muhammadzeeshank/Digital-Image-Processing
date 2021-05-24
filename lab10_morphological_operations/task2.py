import numpy as np
import cv2
from numpy.lib.arraypad import pad
from functions import erosion, dilation

img = cv2.imread('images/fingerprint.tif', 0)
# structuring element
struct_element = np.ones((3, 3), np.uint8)
# applying erosion
eroded_img = erosion(img, struct_element)
final_img = dilation(eroded_img, struct_element)
cv2.imwrite('images/results/task2_img.jpg', final_img)
