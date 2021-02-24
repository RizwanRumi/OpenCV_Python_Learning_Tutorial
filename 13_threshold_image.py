import cv2 as cv
import numpy as np

img = cv.imread('images/gradient.png')
_, th1 = cv.threshold(img, 100, 255, cv.THRESH_BINARY) # val < 100 ,val = 0 and val > 100, val = 255
_, th2 = cv.threshold(img, 100, 255, cv.THRESH_BINARY_INV) # inverse of binary
_, th3 = cv.threshold(img, 120, 255, cv.THRESH_TRUNC) # o - 120 = unchange and 120 - 255 = set by 120
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

cv.imshow('image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)
cv.imshow('th4', th4)
cv.imshow('th5', th5)

cv.waitKey(0)
cv.destroyAllWindows()
