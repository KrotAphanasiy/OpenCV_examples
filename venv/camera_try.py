import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    ret_hsv, frame_hsv = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)

    blurred = cv.GaussianBlur(gray, (13, 13), 0)
    edged = cv.Canny(blurred, 15, 130)


    cnts, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame, cnts, -1, (0, 255, 0), 2)

    hsv = cv.cvtColor(frame_hsv, cv.COLOR_BGR2HSV)
    blurred_hsv = cv.GaussianBlur(hsv, (5,5), 0)
    edged_hsv = cv.Canny(blurred_hsv, 15, 130)

    cnts_hsv, _ = cv.findContours(edged_hsv, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame_hsv, cnts_hsv, -1, (0, 255, 0), 1)


    cv.imshow('Video from gray', frame)
    cv.imshow('Video from hsv', frame_hsv)
    cv.imshow('Blurred', blurred)
    cv.imshow('HSV', hsv)

    if cv.waitKey(1) & 0xFF  == ord('q'):
        break


cap.release()
cv.destroyAllWindows()

