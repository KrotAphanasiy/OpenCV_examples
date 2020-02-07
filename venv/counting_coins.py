from __future__ import print_function
import numpy as np
import argparse
import cv2 as cv

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

image = cv.imread(args["image"])
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (11, 11), 0)
cv.imshow("Image", blurred)

edged = cv.Canny(blurred, 30, 150)
cv.imshow("Edged", edged)
cv.waitKey()

cnts, _ = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(len(cnts))

coins = image.copy()
cv.drawContours(coins, cnts, -1, (0, 255, 0), 2)
cv.imshow("Coins", coins)


for (i, c) in enumerate(cnts):
    (x, y, w, h) = cv.boundingRect(c)
    print("Coin #{}".format(i + 1))
    coin = image[y:y + h, x:x + w]
    cv.imshow("Coin", coin)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    ((centerX, centerY), radius) = cv.minEnclosingCircle(c)
    cv.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    cv.imshow("Masked Coin", cv.bitwise_and(coin, coin, mask=mask))

    cv.waitKey()
    cv.destroyWindow("Coin")
    cv.destroyWindow("Masked Coin")


cv.waitKey()
cv.destroyAllWindows()
