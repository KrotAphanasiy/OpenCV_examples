from __future__ import print_function
import numpy as np
import argparse
import cv2 as cv


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required= True, help="Path to image")
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)
cv.waitKey()

print("max of 255 : {}".format(cv.add(np.uint8([200]), np.uint8([100]))))
cv.waitKey()

print("min of 0 : {}".format(cv.subtract(np.uint8([50]), np.uint8([100]))))
cv.waitKey()

M = np.ones(image.shape, dtype="uint8") * 100
added = cv.add(image, M)
cv.imshow("Added", added)
cv.waitKey()

M = np.ones(image.shape, dtype="uint8") * 50
substracted = cv.subtract(image, M)
cv.imshow("Substracted", substracted)
cv.waitKey()


