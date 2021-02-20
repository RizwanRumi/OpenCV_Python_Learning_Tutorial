import cv2

cap = cv2.VideoCapture(0)

print(cap.get(3)) # cv2.CAP_PROP_FRAME_WIDTH = 3
print(cap.get(4)) # cv2.CAP_PROP_FRAME_HEIGHT = 4

# customize pixel setting and it will differ
cap.set(3, 5000)
cap.set(4, 300)

print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()