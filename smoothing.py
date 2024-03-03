import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
# Computes intensity of center pixel by averaging all surrounding pixels
average = cv.blur(img, (3, 3))
cv.imshow('Average', average)

# Gaussian Blur
# Each surrounding pixel is given a weight and the average of the products gives value for true center
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
# Same as averaging, except it finds median of surrounding pixels rather than averages
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
# Retains edges
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)

