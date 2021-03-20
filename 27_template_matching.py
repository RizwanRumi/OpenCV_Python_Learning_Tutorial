import cv2
import numpy as np

'''
https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
'''


img = cv2.imread("images/messi5.jpg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template_image = cv2.imread("images/messi_face.jpg", 0)
w, h = template_image.shape[::-1] # (width = x, height = y)

res = cv2.matchTemplate(gray_image, template_image, cv2.TM_CCOEFF_NORMED)
print(res)

threshold = 0.9
loc = np.where(res >=threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,255,0), 2)


cv2.imshow('main', img)
#cv2.imshow('main_gray', gray_image)
#cv2.imshow('template', template_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


