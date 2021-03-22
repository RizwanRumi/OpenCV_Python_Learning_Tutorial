import cv2
import numpy as np

# implementation: The standard Hough line Transformation

img = cv2.imread("images/sudoku.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3) # 50- first threshold, 150- second threshold
lines = cv2.HoughLines(edges, 1, np.pi/180, 200) # 1 = rho (distance resolution of the accumulator in pixels), angle, threshold (return greater than values)

# each line will be polar coordinate, either rho, theta, votes or only rho, theta
# x = rcos(theta), y = rsin(theta)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x1, y1 stores the rounded off value
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    # x2, y2 stores the rounded off value
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0,0,255), 2)


cv2.imshow("image", img)
cv2.imshow("Canny Edge Detector", edges)
k = cv2.waitKey(0)
cv2.destroyAllWindows()