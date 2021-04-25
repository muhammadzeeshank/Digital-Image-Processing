import numpy as np
import cv2
img1 = cv2.imread('download.png', 0)
_, th1 = cv2.threshold(img1, 127, 1, cv2.THRESH_BINARY)
label = 0
v = [1]
img = np.lib.pad(th1, ((1, 1), (1, 1)), mode='constant',
                 constant_values=(0, 0))
height, width = img.shape
cv2.imshow('img', img)
print(width, height)
labelmatrix = np.zeros([height, width], np.int8)
table = []
# First parse
for y in range(height):
    for x in range(width):
        if img[y][x] == 1:
            if img[y][x-1] != v[0] and img[y-1][x] != v[0]:
                label = label + 1
                labelmatrix[y][x] = label
                table.append([label])
            if img[y][x-1] == v[0] or img[y-1][x] == v[0]:
                labelmatrix[y][x] = label
            if img[y][x-1] == v[0] and img[y-1][x] == v[0]:
                if labelmatrix[y][x-1] == labelmatrix[y-1][x]:
                    labelmatrix[y][x] = label
                else:
                    labelmatrix[y][x] = labelmatrix[y][x-1]
                    table[-1] = None
                    if table[-2] != None:
                        table[-2].append(label)

print(table)
# 2nd parse
for i in range(len(table)):
    if table[i] != None:
        if len(table[i]) > 1:
            for y in range(width):
                for x in range(height):
                    if labelmatrix[y][x] == table[i][1]:
                        labelmatrix[y][x] = table[i][0]

            table[i].pop(1)

# 3rd parse
for val in table:
    if val == None:
        table.remove(val)

print("Number of objects in image are: " + str(len(table)))
cv2.waitKey(0)
cv2.destroyAllWindows()
