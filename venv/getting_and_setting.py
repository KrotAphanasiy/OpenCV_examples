import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to load image from")
args = vars(ap.parse_args())


image = cv.imread(args["image"])
cv.imshow("Original", image)
cv.waitKey(0)

(b, g, r) = image[0,0]
print("Pixel at (0,0): red: {} green: {} blue: {}".format(r, g, b))


image[0, 0] = (0, 0, 255)
(b, g, r) = image[0,0]
print("Pixel at (0,0): red: {} green: {} blue: {}".format(r, g, b))
cv.waitKey(0)


corner = image[0:100, 0:100]
cv.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

cv.imshow("Updated", image)
cv.waitKey(0)



