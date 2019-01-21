import cv2 as cv
import numpy as np


img =cv.imread('E:/demo/images/cat.jpg')
new =cv.resize(img,None,fx=0.5,fy=0.5,interpolation=cv.INTER_CUBIC)
cv.namedWindow('new')
cv.imshow('new',new)
k =cv.waitKey(0)
if k == ord('s'):#若按下s
   cv.destroyAllWindows()