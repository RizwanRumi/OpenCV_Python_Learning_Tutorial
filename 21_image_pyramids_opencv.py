import cv2
import numpy as np

'''
Pyramid: multi-scale signal representation in which a signal 
is subject to repeated smoothing and subsampling.
1. Laplacian pyramid
2. Gaussian pyramid
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
    cv2.imshow(str(i), layer)

cv2.waitKey(0)
cv2.destroyAllWindows()
