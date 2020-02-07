import numpy as np
import argparse
import cv2 as cv
import imutils
import imutils_my

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("-i", "--image", required=True, help="Path to image")
arguments = vars(argument_parser.parse_args())

image = cv.imread(arguments["image"])
cv.imshow("Original", image)
cv.waitKey()

shifted = imutils_my.transltion(image, -60, 100)
cv.imshow("Shifted", shifted)
cv.waitKey()

rotated = imutils_my.rotate(image, 45)
cv.imshow("Rotated", rotated)
cv.waitKey()

resized = imutils_my.resize(image, 150, cv.INTER_AREA)
cv.imshow("Resized", resized)
cv.waitKey()



