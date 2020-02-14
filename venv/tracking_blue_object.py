from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2 as cv
import imutils
import time

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=False,
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", required=False, type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())


blueLower = (100, 100, 100)
blueUpper = (120, 255, 255)
pts = deque(maxlen=args["buffer"])

if not args.get("video", False):
    vs = VideoStream(0).start()

else:
    vs = cv.VideoCapture(args["video"])

time.sleep(2)

while True:
    frame = vs.read()

    frame = frame[1] if args.get("video", False) else frame
    if frame is None:
        break

    frame = imutils.resize(frame, width=1080)
    blurred = cv.GaussianBlur(frame, (11, 11), 0)
    hsv = cv.cvtColor(blurred, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, blueLower, blueUpper)
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
            cv.circle(frame, (int(x), int(y)), int(radius),
                       (0, 255, 255), 2)
            cv.circle(frame, center, 5, (0, 0, 255), -1)

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
    key = cv.waitKey(1) & 0xFF
    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
    vs.stop()
# otherwise, release the camera
else:
    vs.release()
# close all windows
cv.destroyAllWindows()