import numpy as np
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("--image", "-i", required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
cv.imshow("Original", image)
cv.waitKey()

mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv.rectangle(mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, - 1)
cv.imshow("Mask", mask)
cv.waitKey()

masked = cv.bitwise_and(image, image, mask = mask)
imshow = cv.imshow("Masked", masked)
cv.waitKey()