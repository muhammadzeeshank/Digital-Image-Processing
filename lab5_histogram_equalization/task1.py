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


def contrastStretching(img):
    min = np.percentile(img, 5)
    max = np.percentile(img, 95)
    rows = img.shape[0]
    cols = img.shape[1]
    for i in range(rows):
        for j in range(cols):
            if img[i][j] < min:
                img[i][j] = 0
            elif img[i][j] > max:
                img[i][j] = 255
            else:
                img[i][j] = ((img[i][j] - min)/(max - min))*255
    return img


img = cv.imread('einstein.tif', 0)  # image read
plotHistogram(img, "Original Image")
cv.imshow("Orginal Image", img)
enhanced_image = contrastStretching(img)
plotHistogram(enhanced_image, "Enhanced Image")
cv.imshow("Enhanced image", enhanced_image)
cv.waitKey(0)
cv.destroyAllWindows()
