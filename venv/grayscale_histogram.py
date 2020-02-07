from __future__ import print_function
import numpy as np
import argparse
import cv2 as cv
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())


image = cv.cvtColor(cv.imread(args["image"]), cv.COLOR_BGR2GRAY)
cv.imshow("Image", image)
cv.waitKey()

hist = cv.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv.waitKey()



