import cv2 as cv

# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)

# Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # breaks out of loop if d is pressed
    if cv.waitKey(20) &0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



