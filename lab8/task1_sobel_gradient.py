import numpy as np
import cv2
from tqdm import tqdm  # for progress bar
import matplotlib.pyplot as plt


def sobelOperator(img):
    blurred_img = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
    sobelx = cv2.Sobel(blurred_img, cv2.CV_8U, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred_img, cv2.CV_8U, 0, 1, ksize=3)
    gr_magnitude = np.sqrt(np.square(sobelx) + np.square(sobely))
    g_magnitude = np.uint8(gr_magnitude)
    g_phase = np.divide(sobely, sobelx)
    g_phase = np.rad2deg(np.arctan(g_phase))
    g_phase = np.uint8(g_phase)
    max = g_magnitude.max()
    rows, cols = g_magnitude.shape
    # selecting the lines that are on 45 and 90 degrees and have top 30% magnitude
    for i in tqdm(range(rows)):
        for j in range(cols):
            if (g_magnitude[i][j] > 0.7*max) and (g_phase[i][j] == 45 or g_phase[i][j] == 90):
                continue
            else:
                g_magnitude[i][j] = 0
    return g_magnitude


img = cv2.imread('images/fig1.tif', 0)
final_img = sobelOperator(img)
plt.imshow(final_img, cmap='gray')
plt.title("Gradient Mag")
plt.show()
