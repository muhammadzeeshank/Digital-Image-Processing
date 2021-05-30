import numpy as np
import cv2
from functions import erosion, dilation

img = cv2.imread('images/headCT.tif', 0)
# structuring element
struct_element = np.ones((3, 3), np.uint8)
# applying erosion
eroded_img = erosion(img, struct_element)
# applying dilation
dilated_img = dilation(img, struct_element)

final_img = dilated_img - eroded_img
cv2.imwrite('images/results/task3_img.jpg', final_img)
