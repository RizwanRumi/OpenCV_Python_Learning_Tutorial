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

path = glob.glob("E:/OpenCV_Python_Learning_Tutorial/images/road.png")
image = cv2.imread(path[0])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height), (width/2, height/2), (width, height)
]

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = image.shape[2]
    match_mask_color = (255,) * channel_count
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

cropped_image = region_of_interest(image,
                np.array([region_of_interest_vertices], np.int32))

plt.imshow(cropped_image)
plt.show()