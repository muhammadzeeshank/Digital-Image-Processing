import cv2
import numpy as np


def logTransform(img):
    c = 255 / np.log(1 + np.max(img))
    log_image = c * (np.log(img + 1))
    return log_image


img = cv2.imread('images/blown_ic.tif', 0)

# Taking fourier Transform
img_fft = np.fft.fft2(img)

# Shifting DC componenet to Center
img_fft_shifted = np.fft.fftshift(img_fft)

# taking absolute values
img_fft_shfited_abs = np.abs(img_fft_shifted)

# Taking log transformation
loged_img = logTransform(img_fft_shfited_abs)

# Normalizing image
norm = np.zeros((800, 800))
normalized_img = cv2.normalize(
    loged_img, norm, 0, 255, cv2.NORM_MINMAX)

# Saving Image
cv2.imwrite('images/results/task1_output.jpg', normalized_img)
