import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# 1. Paint the image a certain colour
# blank[200:300, 300:400] = 0, 255, 255
# cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (100, 255, 200), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (200, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (100,250), (300,440), (255, 255, 255), thickness=3)

cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, ":3", (225,225), cv.FONT_HERSHEY_TRIPLEX, 3.0, (0, 0, 255), 5)
cv.imshow('Text', blank)

cv.waitKey(0)

