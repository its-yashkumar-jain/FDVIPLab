import cv2
import numpy as np

img=cv2.imread('Practical 5\carbin.jpg',0)
cv2.imshow('input',img)
cv2.waitKey(0)


#binarize the image
binr=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
#define the kernel
kernel=np.ones((3,3),np.uint8)
#invert the image
invert=cv2.bitwise_not(binr)
#dilate the image
dilation=cv2.dilate(invert,kernel,iterations=1)
cv2.imshow("inverted image",invert)
cv2.imshow("dialted image",dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()