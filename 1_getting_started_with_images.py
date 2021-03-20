import cv2

print("OpenCv Version: ", cv2.__version__)

'''
color image has three channels and grayscale image has one channel
'''

img = cv2.imread("images/lena.jpg", -1)
#img = cv2.imread("images/lena.jpg", 0) # grayscale iamge
#print(img)

(b, g, r) = cv2.split(img)
print(b)
print(b.ravel())

# get dimensions of an image
dimensions = img.shape

#height, width, number of channels of an image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)



cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()