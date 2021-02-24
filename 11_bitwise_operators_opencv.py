import numpy as np
import cv2

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

img2 = np.zeros((250, 500, 3), np.uint8)
img2[0:250, 250: 500] = 255

#bitAnd = cv2.bitwise_and(img1, img2)
#bitOr = cv2.bitwise_or(img1, img2)
#bitXOr = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)


cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
#cv2.imshow('bitAnd', bitAnd)
#cv2.imshow('bitOr', bitOr)
#cv2.imshow('bitXOr', bitXOr)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)


cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
