import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "PAth to load image from")
args = vars(ap.parse_args())


image = cv.imread(args["image"])
print("Width: {} pixels, Height: {} pixels, Channels: {}".format(image.shape[1], image.shape[0], image.shape[2]))
cv.imshow("Original", image)
cv.waitKey(0)


