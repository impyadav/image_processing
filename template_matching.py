import cv2
import numpy as np

src_img = cv2.imread('source_matching.jpg')
src_gray = cv2.cvtColor(src_img , cv2.COLOR_BGR2GRAY)

template = cv2.imread('patch.jpg' , 0)
w , h = template.shape[::-1]

res_matrix = cv2.matchTemplate(src_gray , template , cv2.TM_CCOEFF_NORMED)
threshold  = 0.75
pos = np.where( res_matrix >= threshold )

for pt in zip(*pos[::-1]):
    rect = cv2.rectangle(src_img , pt ,  (pt[0]+w , pt[1]+h), (255 , 0 , 0) , 2)

cv2.imshow('src_img' , src_img)
cv2.waitKey(0)
cv2.destroyAllWindows()