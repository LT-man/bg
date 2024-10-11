import cv2
import numpy as np
video = cv2.VideoCapture("green.mp4")
bro = cv2.imread("broke.jpg")
bg = 0
for i in range (60):
    ret, bg = video.read()
while video.isOpened():
    ret, img = video.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array((104, 153, 70))
    upper = np.array((30, 30, 0))
    mask1 = cv2.inRange(hsv, lower, upper)
    lower = np.array((50, 100, 100))
    upper = np.array((70, 255, 255))
    mask2 = cv2.inRange(hsv, lower, upper)
    mask3 = cv2.bitwise_not(mask2)
    result1 = cv2.bitwise_and(bg, bg, mask=mask2)
    result2 = cv2.bitwise_and(img, img, mask=mask3)
    add = cv2.addWeighted(result1, 1, result2, 1, 0)
    cv2.imshow("screen", add)
    k = cv2.waitKey(15)
    if k == 27:
        break
    
