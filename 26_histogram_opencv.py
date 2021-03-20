import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("images/lena.jpg", -1)
#img = np.zeros((200,200), np.uint8)
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)
#b, g, r = cv.split(img)

#cv.imshow('image', img)
#cv.imshow('b', b)
#cv.imshow('g', g)
#cv.imshow('r', r)

#plt.hist(img.ravel(), 256, [0, 256])
#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])

# hist = cv.calcHist([img], [0], None, [256], [0, 256])
# plt.plot(hist)
# plt.show()

color = ('b', 'g', 'r')

for channel,col in enumerate(color):
    hist = cv.calcHist([img], [channel], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.title("Histogram for color scale picture")
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
