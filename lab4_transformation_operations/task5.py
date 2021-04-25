import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread(
    'tungsten.tif', 0)  # image read
dims = img.shape
rows = img.shape[0]  # rows of image
cols = img.shape[1]  # columns of image
Histogram = np.zeros(256)  # Generate an empty array
CDF = np.zeros(256)
print(Histogram.shape)
ranges = np.arange(256)  # Define x axis
pixels = rows*cols
for i in range(rows):
    for j in range(cols):
        k = img[i][j]
        Histogram[k] = Histogram[k] + 1  # Increment
PDF = Histogram/(rows*cols)
for y in range(255):
    CDF[y] = PDF[y] + CDF[y-1]
plt.plot(ranges, CDF)  # plot histogram
plt.xlabel('Pixels')  # X label of graph
plt.ylabel('CDF')  # Y label of graph
plt.title('CDF Histogram')  # Graph Title
plt.show()
