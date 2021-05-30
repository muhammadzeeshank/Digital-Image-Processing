import numpy as np
import cv2
from functions import erosion, dilation

img = cv2.imread('images/rice_image.tif', 0)
# structuring element
struct_element = np.ones((3, 3), np.uint8)
# applying erosion
eroded_img = erosion(img, struct_element)
# applying dilation
fob_img = dilation(eroded_img, struct_element)
# calculating top hat
g_top = img - fob_img
# saving image
cv2.imwrite('images/results/task4_img.jpg', g_top)
