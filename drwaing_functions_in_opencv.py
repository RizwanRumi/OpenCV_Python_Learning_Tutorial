import numpy as np
import cv2

# flag for imread 0 is grayscale, 1 is color, -1 is alpha channel
#img = cv2.imread('lena.jpg', 1)

# create image with numpy zeros method
img = np.zeros([512, 512, 3], np.uint8)

# draw a line
img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 10)  # 44, 96, 147
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

# draw a rectangle
# top left (x1,y1)-> pt1, low right (x2,y2)-> pt2
# thickness -1 set filled color
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), -1)

# draw a circle
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

# text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
