import numpy as np
import cv2
sizeimg = int(input("Enter Image size: "))
img = np.ones([sizeimg, sizeimg, 3])
img.fill(255)
sizebox = round(sizeimg/10)
img[0:sizebox:1, 0:sizebox:1] = [0, 0, 0]
img[0:sizebox:1, sizeimg:-sizebox:-1] = [255, 0, 0]
img[sizeimg:-sizebox:-1, 0:sizebox:1] = [0, 255, 0]
img[sizeimg:-sizebox:-1, sizeimg:-sizebox:-1] = [0, 0, 255]
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
