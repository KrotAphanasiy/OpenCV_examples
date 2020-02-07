import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)

    blurred = cv.GaussianBlur(gray, (9, 9), 0)
    edged = cv.Canny(blurred, 30, 150)

    cnts, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame, cnts, -1, (0, 255, 0), 2)

    cv.imshow('Video', frame)
    cv.imshow('Blurred', blurred)

    if cv.waitKey(1) & 0xFF  == ord('q'):
        break


cap.release()
cv.destroyAllWindows()

