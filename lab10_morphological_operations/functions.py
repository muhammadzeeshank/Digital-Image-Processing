import numpy as np
import cv2


def padImage(img1, size):
    """
    Purpose: Pads image according to size of mask
    : param img1: original image
    : param size: size of Structuring Element
    : return: padded image
    """
    # Padding image
    padsize = int(size/2)
    img = np.lib.pad(img1, ((padsize, padsize), (padsize, padsize)), mode='constant',
                     constant_values=(0, 0))
    return img


def erosion(img1, mask):
    """
    : param img1: the original image
    : param mask: structuring element
    : return: eroded image
    """
    size_mask = mask.shape[0]
    img = padImage(img1, size_mask)
    rows, cols = img1.shape
    eroded_img = np.zeros([rows, cols])
    size = mask.shape[0]
    sum = np.sum(mask)
    for y in range(rows):
        for x in range(cols):
            val = 0
            for i in range(size):
                for j in range(size):
                    val += img[i + y][j + x] * mask[i][j]
            if val == sum:
                eroded_img[y][x] = 255
            else:
                eroded_img[y][x] = 0
    return eroded_img
