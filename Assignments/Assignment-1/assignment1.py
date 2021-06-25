import numpy as np
import cv2
from tqdm import tqdm
img1 = cv2.imread('images/6_right.jpg', 0)  # input image
# equivalent to vset of values except 0 to 21
_, img = cv2.threshold(img1, 21, 1, cv2.THRESH_BINARY)
img = np.lib.pad(img, ((1, 1), (1, 1)), mode='constant',
                 constant_values=(0, 0))
height, width = img.shape
labelmatrix = np.zeros([height, width], np.uint8)
table = []
label = 0
v = [1]
for y in tqdm(range(height)):
    for x in range(width):
        temp = img[y][x]
        xtemp = img[y][x-1]
        ytemp = img[y-1][x]
        temp_label = labelmatrix[y][x]
        xtemp_label = labelmatrix[y][x-1]
        ytemp_label = labelmatrix[y-1][x]
        if img[y][x] == 1:
            if img[y][x-1] != v[0] and img[y-1][x] != v[0]:
                label = label + 1
                labelmatrix[y][x] = label
                table.append([label])
            elif (img[y][x-1] == v[0]) != (img[y-1][x] == v[0]):
                if img[y-1][x] == v[0]:
                    labelmatrix[y][x] = labelmatrix[y-1][x]
                else:
                    labelmatrix[y][x] = labelmatrix[y][x-1]
            elif img[y][x-1] == v[0] and img[y-1][x] == v[0]:
                if labelmatrix[y][x-1] == labelmatrix[y-1][x]:
                    labelmatrix[y][x] = labelmatrix[y][x-1]
                elif labelmatrix[y][x-1] != labelmatrix[y-1][x]:
                    labelmatrix[y][x] = labelmatrix[y][x-1]

for y in range(height):
    for x in range(width):
        if labelmatrix[y][x] > 0:
            labelmatrix[y][x] = 255
# intermediate output in binary
cv2.imwrite("2_intermediate.jpg", labelmatrix)
count = cv2.findContours(labelmatrix, cv2.RETR_EXTERNAL,
                         cv2.CHAIN_APPROX_NONE)[0]
c = max(count, key=cv2.contourArea)
x, y, w, h = cv2.boundingRect(c)
croped_img = img1[y:y+h, x:x+w]
cv2.imwrite("2_final.jpg", croped_img)  # final output in grayscale
cv2.waitKey(0)
cv2.destroyAllWindows()
