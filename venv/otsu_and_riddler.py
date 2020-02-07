from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(image, (5, 5), 0)
cv.imshow("Blurred", blurred)

T = mahotas.thresholding.rc(blurred)
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < T] = 0
thresh = cv.bitwise_not(thresh)
cv.imshow("Thresh",thresh)



cv.waitKey()
