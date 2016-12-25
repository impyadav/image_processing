import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#define video codec
fourcc = cv2.cv.CV_FOURCC(*'XVID')

#Create a video write object

out = cv2.VideoWriter('output.avi' , fourcc , 20.0 , (640,480) , True )

#read the frame and write that into object

while(cap.isOpened()):
    ret , frame = cap.read()

    out.write(frame)

    cv2.imshow('frame' , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
