import cv2
video = cv2.VideoCapture(0)
while video.isOpened():
    ret, img = video.read()
    cv2.imshow("screen", img)
    k = cv2.waitKey(15)
    if k == 27:
        break