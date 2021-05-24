import numpy as np
import cv2
from matplotlib import pyplot as plt

vessel = cv2.imread('images/OTSU_10_left_seg.png', 0)
img = cv2.imread('images/10_left.jpeg', 0)

# Ploting the Histogram of original image
histeq_img = cv2.equalizeHist(img)
cv2.imwrite('images/results/Hist_eq_img.jpg', histeq_img)

# Histogram plot
plt.hist(histeq_img.ravel(), 256, [1, 256])
plt.savefig('images/results/Hist_of_newimg.jpg')

# Thresholding the histogram equalized image
thresh_img = cv2.threshold(histeq_img, 240, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('images/results/Threshed_img.jpg', thresh_img)


# cc labeling using 8 connectivity
connectivity = 8
output = cv2.connectedComponentsWithStats(thresh_img, connectivity, cv2.CV_32S)
# number of labels
num_labels = output[0]
# label matrix
labels = output[1]
# stats matrix
stats = output[2]
vessel_count = 0

print(num_labels)
