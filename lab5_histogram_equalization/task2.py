import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from tqdm import tqdm  # for progress bar


def calHistogram(img):
    dims = img.shape
    rows = img.shape[0]
    cols = img.shape[1]
    Histogram = np.zeros(256)
    ranges = np.arange(256)
    for i in range(rows):
        for j in range(cols):
            k = img[i][j]
            Histogram[k] = Histogram[k]+1
    return [ranges, Histogram, rows, cols]


def saveHistogram(yaxis, title, ranges, htgram, filename):
    plt.plot(ranges, htgram)
    plt.xlabel('Pixels')
    plt.ylabel(yaxis)
    plt.title(title)
    plt.show()
    # plt.savefig(filename)


def originalHistogram(img, title, filename):
    ranges = calHistogram(img)[0]
    Histogram = calHistogram(img)[1]
    saveHistogram('Frequency', title,
                  ranges, Histogram, filename)


def PDFandCDF(img):
    # for pdf
    ranges, Histogram, rows, cols = calHistogram(img)
    pdf = Histogram / (rows * cols)
    saveHistogram('PDF', 'PDF Histogram', ranges, pdf, 'Figure_2.jpg')
    # for cdf
    cdf = np.zeros(256)
    for y in range(255):
        cdf[y] = pdf[y] + cdf[y-1]
    saveHistogram('CDF', 'CDF Histogram', ranges, cdf, 'Figure_3.jpg')
    return [pdf, cdf]


def trans_function(cdf, img):
    tf = np.round(cdf * 255)
    ranges = calHistogram(img)[0]
    saveHistogram('TF', 'Transfer Function', ranges, tf, 'Figure_4.jpg')
    return tf


def replace_Original_pixels(img, tfn):
    tf = tfn.astype('uint8')
    rows = img.shape[0]
    cols = img.shape[1]
    img1 = np.zeros([rows, cols], np.uint8)
    for k in tqdm(range(256)):  # tqdm is used to display progress bar
        for i in range(rows):
            for j in range(cols):
                if img[i][j] == k:
                    img1[i][j] = tf[k]
    cv.imwrite('Figure_5.jpg', img1)
    return img1


img = cv.imread('einstein.tif', 0)
originalHistogram(img, 'Original Historgram', 'Figure_1.jpg')
cdf = PDFandCDF(img)[1]
tf = trans_function(cdf, img)
img1 = replace_Original_pixels(img, tf)
originalHistogram(img1, 'Enhanced Historgram', 'Figure_6.jpg')
cv.waitKey(0)
cv.destroyAllWindows()
