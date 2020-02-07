import numpy as np
import argparse
import cv2 as cv
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow("Original grayscale", image)

eq = cv.equalizeHist(image)

cv.imshow("Equalized grayscale", eq)
cv.waitKey()

