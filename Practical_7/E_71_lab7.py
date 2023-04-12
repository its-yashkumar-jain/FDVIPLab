import cv2
import numpy as np
import matplotlib.pyplot as plt
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

#Canny edge detector
img=cv2.imread('Practical 1\data\lena.png',cv2.IMREAD_GRAYSCALE)
assert img is not None ,'file could not be read,check with'
edges=cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Images'),plt.xticks([]),plt.yticks([])
plt.show()

#Hough Transform
img=cv2.imread('Practical_7\images\parking_lot.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,75,150)
lines=cv2.HoughLinesP(edges,1,np.pi/180,30,maxLineGap=250)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,128),1)
cv2.imshow("linesEdges",edges)
cv2.imshow("linesDetected",img)
cv2.waitKey(0)
cv2.destroyAllWindows()