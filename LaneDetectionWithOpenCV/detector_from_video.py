import cv2
import numpy as np


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
    img = np.copy(img)
    # make a blank image just like original image
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (255, 0, 0), thickness=4)
    # Merge images with some weight
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def process(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]

    region_of_interest_vertices = [
        (0, height), (width/2, height/2), (width, height)
    ]

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    #cv2.imshow('canny', canny_image)

    cropped_image = region_of_interest(canny_image,
                    np.array([region_of_interest_vertices], np.int32))

    #cv2.imshow('cropped', cropped_image)

    lines = cv2.HoughLinesP(cropped_image,
                            rho = 2,
                            theta=np.pi/180,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)

    image_with_Lines = draw_the_lines(image, lines)
    return image_with_Lines


cap = cv2.VideoCapture('Lane.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()