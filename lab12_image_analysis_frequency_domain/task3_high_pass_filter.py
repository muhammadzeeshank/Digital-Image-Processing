import cv2
import numpy as np


def highPass_Freq_Filter(img, cutoff_radius):
    rows, cols = img.shape
    cutoff_size = (cutoff_radius*2, cutoff_radius*2)
    cutoff = np.zeros(cutoff_size)
    padsizex = int(cols/2) - cutoff_radius
    padsizey = int(rows/2) - cutoff_radius
    freq_fil = np.lib.pad(cutoff, ((padsizey, padsizey), (padsizex, padsizex)),
                          mode='constant', constant_values=(1, 1))
    return freq_fil


img = cv2.imread('images/barbara.tif', 0)

# Taking fourier Transform
img_fft = np.fft.fft2(img)

# Shifting DC componenet to Center
img_fft_shifted = np.fft.fftshift(img_fft)

# Filter
freq_fil = highPass_Freq_Filter(img, 30)

# Multiplying image with filter i.e allowing only high frequencies to pass
low_freq_img = freq_fil * img_fft_shifted

# Inverse fourier transform
filtered_img = np.fft.ifft2(low_freq_img)

# taking absolute values
filtered_img_abs = np.abs(filtered_img)

# Saving Image
cv2.imwrite('images/results/task3_output.jpg', filtered_img_abs)
