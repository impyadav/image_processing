import cv2
import numpy as np
import matplotlib.pyplot as plt

cp = cv2.VideoCapture(0)

while(True):
    ret , frame = cp.read()

    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame' , frame)
    cv2.imshow('gray' , gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cp.release()
cv2.destroyAllWindows()


