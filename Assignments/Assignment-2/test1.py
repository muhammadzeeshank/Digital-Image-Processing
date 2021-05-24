from PIL import Image, ImageFilter
import numpy as np
import cv2
from tqdm import tqdm
img = cv2.imread('images/10_left.jpeg', 0)
height, width = img.shape
gamma = 1.5
img1 = np.zeros([height, width])
for x in tqdm(range(width)):
    for y in range(height):
        img1[y][x] = 255 * ((img[y][x]/255)**gamma)


cv2.imwrite("images/result10.jpg", img1)


# Importing Image and ImageFilter module from PIL package

# creating a image object
# im1 = Image.open(r'images/result10.jpg')

# # applying the max filter
# for x in range(10):
#     im1 = im1.filter(ImageFilter.MaxFilter(size=7))

# im1.save("images/result10a.jpg", "JPEG")
