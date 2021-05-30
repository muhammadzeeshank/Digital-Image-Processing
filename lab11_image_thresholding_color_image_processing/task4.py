import numpy as np
import cv2
# to convert BGR image to HSV

img = cv2.imread('images/strawberries.tif')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_img)
cv2.imwrite('images/results/task4hues.jpg', h)
cv2.imwrite('images/results/task4saturations.jpg', s)
cv2.imwrite('images/results/task4values.jpg', v)
