import cv2
import numpy as np

'''
first step, movement is difference between two frames 
second, difference has noises because of details and light on video so gaussian blurring is eliminating the noises,
third, obtaining threshold from clean difference
fourth, dilating for eliminating district small weak threshold lines which corrupt healthy threshold detection
fifth, finding contours from clean threshold
sixth, eliminating small contours which can not be a human by filtering contour area
seventh, drawing rectangles for each detected contour on the frame, rectangle dimensions obtained from cv2.boundingRect(contour)   
'''
cap = cv2.VideoCapture('images/vtest.avi')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 700:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10,20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0,0,255), 3)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()