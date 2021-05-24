import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def plotHistogram(img, imgtitle):
    dims = img.shape
    rows = img.shape[0]
    cols = img.shape[1]
    Histogram = [0]*256
    ranges = np.arange(256)
    for i in range(rows):
        for j in range(cols):
            k = img[i][j]
            Histogram[k] = Histogram[k]+1
    plt.plot(ranges, Histogram)
    plt.xlabel('Pixels')
    plt.ylabel('Frequency')
    plt.title(imgtitle)
    plt.show()


img1 = cv.imread('images/result10.jpg', 0)
# plotHistogram(img1, 'histogram')
plt.hist(img1.flat, bins=100, range=(0, 255))
cv.waitKey(0)
cv.destroyAllWindows()
