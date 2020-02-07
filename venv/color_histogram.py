from __future__ import print_function
import numpy as np
import argparse
import cv2 as cv
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())


image = cv.imread(args["image"])
cv.imshow("Original", image)
cv.waitKey()

chans = cv.split(image)
colors = ("b","g","r")

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for(chan, color) in zip(chans, colors):
    hist = cv.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])

plt.show()


fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv.calcHist([chans[1], chans[0]], [0, 1], None, [32,32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "bilinear")
ax.set_title("2D for G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "bilinear")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv.calcHist([chans[0], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "bilinear")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
plt.show(fig)


print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))