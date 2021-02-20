import cv2

#  use external video link e.g: 'myVideo.avi'
# default camera set value 0 or -1
# multiple camera: set value 1 for 2nd camera, 2 for 3rd camera


cap = cv2.VideoCapture(0)

# isOpened() return true or false about the directory of video file path
print(cap.isOpened())

while cap.isOpened():
    # while True:
    ret, frame = cap.read()

    # print some video property : cap.get()
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    #  convert color to gray scale video
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    # cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
