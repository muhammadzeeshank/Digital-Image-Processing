import cv2 as cv
import numpy as np


def distance(p1, p2, c):


if c == 1:
euDst = np.power(np.power((p1[0]-p2[0]), 2) + np.power((p1[1]-p2[1]), 2), 0.5)
print("Euclidean Distance is: " + str(euDst))
if c == 2:
ctyBlock = (np.absolute(p1[0]-p2[0]) + np.absolute(p1[1]-p2[1]))
print("City Block Distance is: " + str(ctyBlock))
if c == 3:
chsBoard = np.maximum(np.absolute(p1[0]-p2[0]), np.absolute(p1[1]-p2[1]))
print("ChessBoard Distance is: " + str(chsBoard))


img = cv.imread("image.png")
cv.imshow("Original Image", img)
height = img.shape[0]
width = img.shape[1]
p = (height-200, width-150)
q = (height-100, width-50)
num = int(input("Enter Choice: "))
distance(p, q, num)
