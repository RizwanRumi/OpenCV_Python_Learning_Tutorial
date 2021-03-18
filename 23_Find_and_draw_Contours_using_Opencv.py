import cv2
import numpy as np

img = cv2.imread('images/opencv-rafiq.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
#contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('Number of contours = ' + str(len(contours)))

# individual contour
print(contours[0])

#cv2.drawContours(img, contours, -1, (0, 255, 0), 3) # -1 = draw all contours
#cv2.drawContours(img, contours, 0, (0, 255, 0), 3) # 0 = draw the first contours
#cv2.drawContours(img, contours, 1, (0, 255, 0), 3) # 1 = draw the second contours
cv2.drawContours(img, contours, 2, (0, 255, 0), 2)

cv2.imshow('Image', img)
#cv2.imshow('Image Gray', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
