import numpy as np
import cv2
import random
from tqdm import tqdm  # for progress bar


def constructMask():
    """
    Purpose: Takes input from user and build a required mask
    : return: mask, size of mask
    """
    # Taking size and value of mask from user
    # Enforcing the user to enter size of mask only in odd number
    while(True):
        size = int(input("Enter mask size(only odd number): "))
        if (size % 2) != 0:
            break
        else:
            print("[-] ERROR. Please Enter odd number!")
    mask = np.zeros([size, size])
    while(True):
        opt = input(
            "Chose one option: \n 1) Mask with constant value \n 2) Mask with variable values \n")
        if opt == '1':
            value = input("Enter maske value(fraction/float/int):")
            value = fractionToFloat(value)
            # filling mask of (size, size) with value
            mask = np.full([size, size], value)
            break
        elif opt == '2':
            for i in range(size):
                for j in range(size):
                    value = input(
                        f"Enter maske value(fraction/float/int) at ({i}, {j}):")
                    mask[i][j] = fractionToFloat(value)
            break
        else:
            print("[-] INVALID INPUT! Please chose 1 or 2")
    return mask, size


def fractionToFloat(value):
    '''
    value: fraction e.g(a/b)
    return: float value
    '''
    if '/' in value:
        num, den = value.split('/')
        value = float(num)/float(den)
    else:
        value = float(value)
    return value


def padImage(img1, size):
    """
    Purpose: Pads image according to size of mask
    : param img1: original image
    : param size: size of mask
    : return: padded image
    """
    # Padding image
    padsize = int(size/2)
    img = np.lib.pad(img1, ((padsize, padsize), (padsize, padsize)), mode='constant',
                     constant_values=(0, 0))
    return img


def applyFilter(img, img1, mask):
    """
    Purpose: Applies filter according to mask size and values
    : param img: the padded image
    : param img1: the original image
    : return: convovled image with mask
    """
    # convolving mask with image
    rows, cols = img1.shape
    img2 = np.zeros([rows, cols])
    size = mask.shape[0]
    for y in tqdm(range(rows)):
        for x in range(cols):
            val = 0
            for i in range(size):
                for j in range(size):
                    val += img[i + y][j + x] * mask[i][j]
            img1[y][x] = val
    return img1


def medianFilter(img, img1, size):
    """
    : param img: the padded image
    : param img1: the original image
    : param size: size of mask
    : return: image with median filter applied
    """
    rows, cols = img1.shape
    for y in tqdm(range(rows)):
        for x in range(cols):
            data = []
            for i in range(size):
                for j in range(size):
                    data.append(img[i+y][j+x])
            img1[y][x] = np.median(data)
    return img1


def minFilter(img, img1, size):
    """
    : param img: the padded image
    : param img1: the original image
    : param size: size of mask
    : return: image with min filter applied
    """
    rows, cols = img1.shape
    for y in tqdm(range(rows)):
        for x in range(cols):
            data = []
            for i in range(size):
                for j in range(size):
                    data.append(img[i+y][j+x])
            img1[y][x] = np.min(data)
    return img1


def maxFilter(img, img1, size):
    """
    : param img: the padded image
    : param img1: the original image
    : param size: size of mask
    : return: image with max filter applied
    """
    rows, cols = img1.shape
    for y in tqdm(range(rows)):
        for x in range(cols):
            data = []
            for i in range(size):
                for j in range(size):
                    data.append(img[i+y][j+x])
            img1[y][x] = np.max(data)
    return img1


def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def combineImages(img1, img2):
    rows, cols = img1.shape
    img = np.zeros([rows, cols], np.float)
    for y in tqdm(range(rows)):
        for x in range(cols):
            img[y][x] = img1[y][x] + img2[y][x]
    return img
