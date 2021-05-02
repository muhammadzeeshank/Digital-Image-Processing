import numpy as np
import cv2
from functions import constructMask, padImage, medianFilter, sp_noise


# **** main ***
folder = 'images'
imagename = 'lenna.png'  # input image name here
imgtoread = folder + '/' + imagename
# Reading image from drive
orig_img = cv2.imread(imgtoread, 0)
# Adding salt and papper noise to image
noise_img = sp_noise(orig_img, 0.05)
# constructing mask
mask, mask_size = constructMask()
# padding image
pad_img = padImage(noise_img, mask_size)
# applying median filter
final_img = medianFilter(pad_img, noise_img, mask_size)
# final image
imagetodisplay = folder + '/' + 'result_' + imagename
cv2.imwrite(imagetodisplay, final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
