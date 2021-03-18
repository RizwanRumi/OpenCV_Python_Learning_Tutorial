import cv2
import numpy as np

'''
Pyramid: multi-scale signal representation in which a signal 
is subject to repeated smoothing and subsampling.
1. Laplacian pyramid
2. Gaussian pyramid

It helps us to blend the images and the reconstruction of the images
'''
# Gaussian pyramid repeats filtering and subsampling the image
img = cv2.imread("images/lena.jpg")
'''
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)
hr2 = cv2.pyrUp(lr2) # make low level image or blur image

cv2.imshow("Original image", img)
cv2.imshow("PyrDown 1 image", lr1)
cv2.imshow("PyrDown 2 image", lr2)
cv2.imshow("PyrUp 1 image", hr2)
'''
# re-write this code using for loop

cv2.imshow("Original image", img)

layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    #cv2.imshow(str(i), layer)

# Laplacian: A level in Laplacian Pyramid is formed by the difference
# between that level in gaussian pyramid and expanded version of its
# upper level in Gaussian pyramid.

layer = gp[5]
cv2.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()


