import numpy as np
import cv2

img = cv2.imread("img2.jpg", 0)
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("rotated image", img)
cv2.imwrite("rotatedimg.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
