import cv2
import numpy as np

apple = cv2.imread("images/apple.jpg")
orange = cv2.imread("images/orange.jpg")

print(apple.shape)
print(orange.shape)

#apple_orange = np.vstack((apple[:256], orange[256:])) # take only row values
apple_orange = np.hstack((apple[:, :256], orange[:, 256:])) # take column values


# generate Gaussian pyramid for apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)


# generate Gaussian pyramid for orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)


# generate Laplacian pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)


# generate Laplacian pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)


# Now add left and right halves of images in each level
apple_orange_pyramid_lr = []

apple_orange_pyramid_ud = [] # and up and down halves
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian_left_right = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):])) # for left and right halves
    laplacian_up_down = np.vstack((apple_lap[0:int(rows/2), :], orange_lap[int(cols/2):, :])) # for up and down halves
    apple_orange_pyramid_lr.append(laplacian_left_right)
    apple_orange_pyramid_ud.append(laplacian_up_down)

# now reconstruct
apple_orange_reconstruct_lr = apple_orange_pyramid_lr[0]
apple_orange_reconstruct_ud = apple_orange_pyramid_ud[0]

for i in range(1, 6):
    apple_orange_reconstruct_lr = cv2.pyrUp(apple_orange_reconstruct_lr)
    apple_orange_reconstruct_lr = cv2.add(apple_orange_pyramid_lr[i], apple_orange_reconstruct_lr)

    apple_orange_reconstruct_ud = cv2.pyrUp(apple_orange_reconstruct_ud)
    apple_orange_reconstruct_ud = cv2.add(apple_orange_pyramid_ud[i], apple_orange_reconstruct_ud)


#cv2.imshow("apple", apple)
#cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_reconstruct_left_right", apple_orange_reconstruct_lr)
cv2.imshow("apple_orange_reconstruct_up_down", apple_orange_reconstruct_ud)

cv2.waitKey(0)
cv2.destroyAllWindows()