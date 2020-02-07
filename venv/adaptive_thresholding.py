import numpy as np
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.bilateralFilter(image, 7, 21, 21)
cv.imshow("Image", image)
cv.imshow("Blurred", blurred)


thresh = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 4)
cv.imshow("Mean Thresh", thresh)

thresh = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 3)
cv.imshow("Gaussian thresh", thresh)

cv.waitKey()