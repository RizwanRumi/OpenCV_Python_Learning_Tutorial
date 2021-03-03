import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
Morphology is a broad set of image processing operations that 
process images based on shapes. Morphological operations apply 
a structuring element to an input image, creating an output 
image of the same size. In a morphological operation, the value 
of each pixel in the output image is based on a comparison of 
the corresponding pixel in the input image with its neighbors.
'''


#img = cv2.imread('images/smarties.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/j.png', cv2.IMREAD_GRAYSCALE)

'''
masking: 1) identify a unique shape or feature of the object
that you want to detect
'''

# j.png is a binary image ,so don't need to apply mask
# _, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

mask = img # use this because of changing variable will take time :)

print(img)
print('------')
#print(mask)

'''
kernel is normally a shape, which is applied on image.

Dilation: add pixels to the boundaries of objects in an image and 
it depends on the shape of the structuring element used to process 
the image.
'''

kernal = np.ones((5,5), np.uint8)

dilation = cv2.dilate(mask, kernel=kernal, iterations=2)

'''
erosion: remove pixels on object boundaries and so when this erosion 
is applied, the kernel which we have defined slides through all the image 
and a pixel in the original image either 1 or 0 will be considered as 1 only 
if all pixels under the kernel is 1 otherwise it is eroded and this means this 
value will be set to 0 zero which means this will be a black area
'''

erosion = cv2.erode(mask, kernel=kernal, iterations=1)
# opening -> erosion first and then followed by dilation
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)
# closing -> dilation first and then followed by erosion
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE, kernal)
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

titles = ['images', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()