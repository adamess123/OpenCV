import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0]) # width, height respectively
    return cv.warpAffine(img, transMat, dimensions)

# negative x --> left
# negative y --> up
# positive x --> right
# positive y --> down

translated = translate(img, -100, 100)
cv.imshow("Translated", translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    # Assumes center rotation if no rotation point provided
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow("Rotated Rotated", rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
# Flip Codes: 0 - Vertical, 1 - Horizontal, -1 - Vertical AND Horizontal
flip0 = cv.flip(img, 0)
flip1 = cv.flip(img, 1)
flipneg1 = cv.flip(img, -1)

cv.imshow('Flip 0', flip0)
cv.imshow('Flip 1', flip1)
cv.imshow('Flip -1', flipneg1)

# Cropping
cropped = img[200:400, 300:500]
cv.imshow("Cropped", cropped)

cv.waitKey(0)