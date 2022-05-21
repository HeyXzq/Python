import cv2

img = cv2.imread('./cartoon.jpg')

cv2.imshow('my example image', img)

cv2.waitKey(0)