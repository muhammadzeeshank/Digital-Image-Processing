import numpy as np
import cv2
from functions import constructMask, padImage, applyFilter, combineImages


# **** main ***
folder = 'images'
imagename = 'circuit.png'  # input image name here
imgtoread = folder + '/' + imagename
# Reading image from drive
orig_img = cv2.imread(imgtoread, 0)
# constructing mask
mask, mask_size = constructMask()
print(f'Applying maske \n {mask}')
# padding image
pad_img = padImage(orig_img, mask_size)
# applying median filter
filtered_img = applyFilter(pad_img, orig_img, mask)
# combining filtered and original image
final_img = combineImages(orig_img, filtered_img)
# final image
imagetodisplay = folder + '/' + 'result_' + imagename
cv2.imwrite(imagetodisplay, final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
