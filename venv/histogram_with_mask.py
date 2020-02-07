from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2 as cv

def plot_histogram(image, title, mask = None):
    chans = cv.split(image)
    colors = ("b","g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")

    for (chan, color) in zip(chans, colors):
        hist = cv.calcHist([chan], [0], mask, [256], [0, 256])
        plt.plot(hist, color = color)
        plt.xlim([0,256])


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)
plot_histogram(image, "Hist for original image", None)

mask = np.zeros(image.shape[:2], dtype="uint8")
cv.rectangle(mask, (100, 100), (300, 300), 255, -1)

masked = cv.bitwise_and(image, image, mask = mask)
cv.imshow("Masked image", masked)
plot_histogram(masked, "Histogram for masked", mask = mask)

plt.show()
cv.waitKey()


