import cv2
import numpy as np

img1 = cv2.imread('pythonlogo.png')
img2 = cv2.imread('matplot.jpg')


rows , cols , chnl = img1.shape
roi = img2[0:rows , 0:cols]

img2_new = img2[0:280 , 0:280]


img1gray = cv2.cvtColor(img1  , cv2.COLOR_BGR2GRAY)

ret , mask  = cv2.threshold(img1gray , 220 , 255 , cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img2_bg = cv2.bitwise_and(roi , roi , mask = mask_inv)
img1_fg = cv2.bitwise_and(img2_new , img2_new , mask = mask)

dst = cv2.add(img1_fg , img2_bg)


cv2.imshow('dst' , dst)
cv2.waitKey(0)
cv2.destroyAllWindows()






