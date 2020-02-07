import numpy as np
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.bilateralFilter(image, 5, 21, 21)
blurred = cv.equalizeHist(blurred)
cv.imshow("image", image)
cv.imshow("Blurred and equalized", blurred)

(T, thresh) = cv.threshold(blurred, 130, 255, cv.THRESH_BINARY)
cv.imshow("Treshold binary", thresh)

(T, threshInv) = cv.threshold(blurred, 130, 255, cv.THRESH_BINARY_INV)
cv.imshow("ThrshInv", threshInv)

cv.imshow("Cat", cv.bitwise_and(image, image, mask = threshInv))

cv.waitKey()