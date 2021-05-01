import numpy as np
import cv2
from functions import constructMask, padImage, applyFilter, minFilter


# **** main ***
folder = 'images'
imagename = 'img1b.tif'  # input image name here
imgtoread = folder + '/' + imagename
# Reading image from drive
orig_img = cv2.imread(imgtoread, 0)
mask, mask_size = constructMask()
pad_img = padImage(orig_img, mask_size)
final_img = minFilter(pad_img, orig_img, mask_size)
# # final image
imagetodisplay = folder + '/' + 'result_' + imagename
cv2.imwrite(imagetodisplay, final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
