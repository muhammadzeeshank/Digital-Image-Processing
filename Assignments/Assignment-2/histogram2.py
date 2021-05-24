import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/10_left.jpeg', 0)
plt.hist(img.ravel(), 256, [1, 256])
plt.savefig()
