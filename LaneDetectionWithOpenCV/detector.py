import cv2
import matplotlib.pylab as plt
import numpy as np
import glob

'''
to get multiple images:
path = glob.glob("E:/OpenCV_Python_Learning_Tutorial/images/*.png")

for file in path:
    print(file)
    img = cv2.imread(file)
'''


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = image.shape[2]
    # match_mask_color = (255,) * channel_count
    match_mask_color = 255 # because of one channel in grayscale image
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_the_lines(img, lines):
    #cv2.imshow('copy', img)
    #copy_img = np.copy(img)
    # make a blank image just like original image
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (255, 0, 0), thickness=4)
    # Merge images with some weight
    copy_img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return copy_img


path = glob.glob("E:/OpenCV_Python_Learning_Tutorial/images/road.png")
image = cv2.imread(path[0])
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height), (width/2, height/2), (width, height)
]

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_image = cv2.Canny(gray_image, 100, 200)
#cv2.imshow('canny', canny_image)

cropped_image = region_of_interest(canny_image,
                np.array([region_of_interest_vertices], np.int32))

cv2.imshow('cropped', cropped_image)

lines = cv2.HoughLinesP(cropped_image,
                        rho = 6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25)

image_with_Lines = draw_the_lines(image, lines)

plt.imshow(image_with_Lines)
plt.show()