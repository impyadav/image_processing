import cv2
import numpy as np

img = cv2.imread('flowers.jpg')

kernel = np.ones((9,9) , np.float32)/81

convo = cv2.filter2D(img , -1  , kernel)

gauss = cv2.GaussianBlur(img , (9,9) , 0)



cv2.imshow('img' , img)
cv2.imshow('convo' , convo)
cv2.imshow('gauss' , gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()