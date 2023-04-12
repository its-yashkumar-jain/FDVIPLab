import cv2
import numpy as np
#Horizontal lines
img=cv2.imread('Practical 5\lines.png',0)
cv2.imshow('orginal',img)
kernel=np.ones((2,16),np.uint8)
horizontal_lines=cv2.erode(img,kernel,iterations=1)
cv2.imshow("output",horizontal_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Vertical lines
kernel=np.ones((11,3),np.uint8)
vertical_lines=cv2.erode(img,kernel,iterations=1)
cv2.imshow('orginal',img)
cv2.imshow("vertical",vertical_lines)
cv2.waitKey(0)
cv2.destroyAllWindows()