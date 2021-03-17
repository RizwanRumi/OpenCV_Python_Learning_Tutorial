import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('images/messi5.jpg', 0)

canny = cv.Canny(img, 100, 200)

titles = ['image', 'canny']
images = [img, canny]

for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

'''
def nothing(x):
    print(x)

cv.namedWindow('image')

cv.createTrackbar('start', 'image', 0, 200, nothing)
cv.createTrackbar('end', 'image', 0, 300, nothing)

while 1:
    img = cv.imread('images/messi5.jpg', 0)
    start = cv.getTrackbarPos('start', 'image')
    end = cv.getTrackbarPos('end', 'image')

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    if start == 0 and end == 0:
        pass
    else:
        img = cv.Canny(img, start, end)

    img = cv.imshow('image', img)
    
cv.destroyAllWindows()
'''
