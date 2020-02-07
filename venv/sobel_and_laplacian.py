import numpy as np
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#image = cv.equalizeHist(image)
cv.imshow("Original", image)

lap = cv.Laplacian(image, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

sobelX = cv.Sobel(image, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(image, cv.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelcombined = cv.bitwise_or(sobelY, sobelX)

cv.imshow("Soble", sobelcombined)


cv.waitKey()
