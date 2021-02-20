import cv2

print("OpenCv Version: ", cv2.__version__)


img = cv2.imread("lena.jpg", 1)

# print(img)

cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()