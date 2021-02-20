import cv2

#  use external video link e.g: 'myVideo.avi'
# default camera set value 0 or -1
# multiple camera: set value 1 for 2nd camera, 2 for 3rd camera


cap = cv2.VideoCapture(0);

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
