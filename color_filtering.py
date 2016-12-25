import cv2
import numpy as np

cap =  cv2.VideoCapture(0)

while(True):

    ret , frame =  cap.read()

    hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lower_red = np.array([110,50,50])

    upper_red = np.array([130,255,255])

    mask  = cv2.inRange(hsv_frame , lower_red , upper_red)

    result = cv2.bitwise_and(frame , frame , mask = mask)

    cv2.imshow('frame' , frame)
    cv2.imshow('hsv_frame' , hsv_frame)
    cv2.imshow('mask', mask)

    k = cv2.waitKey(5) & 0xFF

    if k == 27 :
        break

cv2.destroyAllWindows()
cap.release()