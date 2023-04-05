import cv2
import numpy as np

img=cv2.imread('Practical 5\eight.jpg',0)
img = cv2.resize(img, (256, 256))
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

#define the kernel
kernel1=np.ones((3,3),np.uint8)
kernel2=np.ones((5,5),np.uint8)
#erode the image
erosion3=cv2.erode(invert,kernel1,iterations=1)
erosion5=cv2.erode(invert,kernel2,iterations=1)
cv2.imshow("inverted image",invert)
cv2.imshow("erode3 image",erosion3)
cv2.imshow("erode5 image",erosion5)
cv2.waitKey(0)
cv2.destroyAllWindows()

img=cv2.imread('Practical 5\h5.jpg',0)
img = cv2.resize(img, (256, 256))
cv2.imshow('input',img)
cv2.waitKey(0)


#binarize the image
binr=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
#define the kernel
kernel=np.ones((3,3),np.uint8)
#opening the image
opening=cv2.morphologyEx(binr,cv2.MORPH_OPEN,kernel,iterations=30)
cv2.imshow('opening done',opening)
cv2.waitKey(0)

closing=cv2.morphologyEx(binr,cv2.MORPH_CLOSE,kernel,iterations=25)
cv2.imshow('closing done',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()