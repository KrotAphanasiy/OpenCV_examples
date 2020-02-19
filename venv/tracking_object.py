from collections import deque
import numpy as np
import argparse
import cv2 as cv
import imutils
import time

def set_ranges(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(x,y)

        (blue, green, red) = frame[y, x]
        color = np.uint8([[[blue, green, red]]])
        hsv_color = cv.cvtColor(color, cv.COLOR_BGR2HSV)
        hue = hsv_color[0][0][0]

        global  Lower, Upper

        Lower = hue - 10
        Upper = hue + 10


        print(Lower, Upper)


ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=False,
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", required=False, type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())


Lower = 70
Upper = 100
pts = deque(maxlen=args["buffer"])


cap = cv.VideoCapture(0)
cv.namedWindow("Frame")
cv.setMouseCallback("Frame", set_ranges)

#fourcc = cv.VideoWriter_fourcc(*'XVID')
#out = cv.VideoWriter('output.avi',fourcc, 20.0, (640,480))

time.sleep(2)

while True:
    _, frame = cap.read()

    #frame = imutils.resize(frame, width=1080)
    blurred = cv.GaussianBlur(frame, (11, 11), 0)
    hsv = cv.cvtColor(blurred, cv.COLOR_BGR2HSV)

    print(Lower, Upper)
    mask = cv.inRange(hsv, np.uint8([Lower, 100, 100]), np.uint8([Upper, 255, 255]))
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)

    cnts = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv.contourArea)
        ((x, y), radius) = cv.minEnclosingCircle(c)
        M = cv.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        if radius > 10:
            x1 = x - radius - 10
            y1 = y - radius - 10
            x2 = x + radius + 10
            y2 = y + radius + 10
            cv.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    pts.appendleft(center)

    # loop over the set of tracked points
    for i in range(1, len(pts)):
        # if either of the tracked points are None, ignore
        # them
        if pts[i - 1] is None or pts[i] is None:
            continue
        # otherwise, compute the thickness of the line and
        # draw the connecting lines
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
    # show the frame to our screen
    cv.imshow("Frame", frame)
    #out.write(frame)
    key = cv.waitKey(1)
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break


cap.release()
#out.release()
# close all windows
cv.destroyAllWindows()