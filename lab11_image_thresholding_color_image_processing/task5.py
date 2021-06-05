import numpy as np
import cv2
# to apply gaussian and sobel filter on coloured image

img = cv2.imread('images/lenna_rgb.tif')
b, g, r = cv2.split(img)
mask_dim = 13
# applying gaussian blur on each channel
gblured_b = cv2.GaussianBlur(b, (mask_dim, mask_dim), 0)
gblured_g = cv2.GaussianBlur(g, (mask_dim, mask_dim), 0)
gblured_r = cv2.GaussianBlur(r, (mask_dim, mask_dim), 0)

# applying sobel on each channel
sobel_b = cv2.Sobel(b, cv2.CV_64F, 1, 0, ksize=5)
sobel_g = cv2.Sobel(g, cv2.CV_64F, 1, 0, ksize=5)
sobel_r = cv2.Sobel(r, cv2.CV_64F, 1, 0, ksize=5)

# merging all channels
gblured_img = cv2.merge((gblured_b, gblured_g, gblured_r))
sobel_img = cv2.merge((sobel_b, sobel_g, sobel_r))

# s saving images
cv2.imwrite('images/results/task5gaussianimg.jpg', gblured_img)
cv2.imwrite('images/results/task5sobelimg.jpg', sobel_img)
