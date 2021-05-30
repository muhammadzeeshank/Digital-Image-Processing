import numpy as np
import cv2


def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    cmax = max(r, g, b)    # maximum of r, g, b
    cmin = min(r, g, b)    # minimum of r, g, b
    diff = cmax-cmin       # diff of cmax and cmin.
    # if cmax and cmax are equal then h = 0
    if cmax == cmin:
        h = 0
    # if cmax equal r then compute h
    elif cmax == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    # if cmax equal g then compute h
    elif cmax == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    # if cmax equal b then compute h
    elif cmax == b:
        h = (60 * ((r - g) / diff) + 240) % 360
    # if cmax equal zero
    if cmax == 0:
        s = 0
    else:
        s = (diff / cmax) * 100
    # compute v
    v = cmax * 100
    return h, s, v


def rgbImage_to_HsvSepImages(image):
    b, g, r = cv2.split(image)
    rows, cols = r.shape
    h = np.zeros([rows, cols])
    s = np.zeros([rows, cols])
    v = np.zeros([rows, cols])
    for i in range(rows):
        for j in range(cols):
            h[i, j], s[i, j], v[i, j] = rgb_to_hsv(r[i, j], g[i, j], b[i, j])
    return h, s, v


img = cv2.imread('images/strawberries.tif')
hs, ss, vs = rgbImage_to_HsvSepImages(img)
cv2.imwrite('images/results/task3hues.jpg', hs)
cv2.imwrite('images/results/task3saturations.jpg', ss)
cv2.imwrite('images/results/task3values.jpg', vs)
