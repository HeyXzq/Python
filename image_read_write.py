import cv2

image = cv2.imread('./cartoon.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('grayscale image', image)

cv2.waitKey(3000)


img = cv2.imread('./cartoon.jpg')

cv2.imshow('my example image', img)

cv2.waitKey(3000)
