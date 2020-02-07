import cv2 as cv
import numpy as np

canvas = np.zeros((300,300,3), dtype="uint8")


green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

cv.line(canvas, (0,0), (300, 300), green)
cv.line(canvas, (0,300), (300, 0), red)
cv.rectangle(canvas, (10,10), (60,60), green)
cv.rectangle(canvas, (200,200), (250,300), red, 5)
cv.rectangle(canvas, (100,100), (150,150), blue, -1)
cv.imshow("Canvas", canvas)
cv.waitKey(0)

canvas = np.zeros((300,300,3), dtype="uint8")

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

for r in range (0, 175, 25):
    cv.circle(canvas, (centerX, centerY), r, white)


cv.imshow("Circles", canvas)
cv.waitKey(0)

canvas = np.zeros((300,300,3), dtype="uint8")


for i in range (0, 200):
    radius = np.random.randint(5, high = 50)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt =  np.random.randint(0, high = 300, size = (2,))
    cv.circle(canvas, tuple(pt), radius, color, -1)


cv.imshow("Random circles", canvas)
cv.waitKey(0)


