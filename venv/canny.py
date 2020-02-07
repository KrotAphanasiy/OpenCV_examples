import numpy as np
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

original = cv.imread(args["image"])
image = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
image = cv.GaussianBlur(image, (7,7), 0)
cv.imshow("Blurred", image)

canny = cv.Canny(image, 30, 150)
cv.imshow("Canny", canny)

zeros = np.zeros(image.shape[:2], dtype= "uint8")

green_edges = cv.merge([zeros, canny, zeros])
edged = cv.bitwise_or(original, green_edges)

cv.imshow("Edged", edged)

cv.waitKey()