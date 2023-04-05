import cv2
import numpy as np

image = cv2.imread('Practical 5\mri.jpg', 0)
image = cv2.resize(image, (200, 200))
#Low pass Filter
#prepare the 5x5 shaped filter

kernel = np.array([[1,1,1,1,1],
                   [1,1,1,1,1],
                   [1,1,1,1,1],
                   [1,1,1,1,1],
                   [1,1,1,1,1]])
#prepare 3x3 filter
kernel3 = np.array([[1,1,1],
                   [1,1,1],
                   [1,1,1],])
kernel=kernel/sum(kernel)
kernel3=kernel3/sum(kernel3)
#filter the source image
img_fil=cv2.filter2D(image,-1,kernel)
img_fil2=cv2.filter2D(image,-1,kernel3)
cv2.imshow('Orginal Image', image)
cv2.imshow('Filtered Image 5', img_fil)
cv2.imshow('Filtered Image 3', img_fil2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#High pass filter
image1 = cv2.imread('Practical 2\data\cameraman.jpg', 0)
high_kernel=np.array([[0.0,-1.0,0.0],
                     [-1.0,4.0,-1.0],
                     [0.0,-1.0,0.0]])
high_kernel5=np.array([[-1,-1,-1,-1,-1],
                       [-1,1,2,1,-1],
                       [-1,2,4,2,-1],
                       [-1,1,2,1,-1],
                       [-1,-1,-1,-1,-1]
                       ])
high_kernel=high_kernel/(np.sum(high_kernel) if np.sum(high_kernel)!=0 else 1)
high_kernel5=high_kernel5/(np.sum(high_kernel5) if np.sum(high_kernel5)!=0 else 1)
#filter the sorce image
img_filh=cv2.filter2D(image1,-1,high_kernel)
img_filh2=cv2.filter2D(image1,-1,high_kernel5)
cv2.imshow('Orginal Image', image1)
cv2.imshow('Filtered High pass Image 3', img_filh)
cv2.imshow('Filtered High pass Image 5', img_filh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

noisy = cv2.imread('Practical 5/noisy.jpg', 0)
m,n=noisy.shape


#Traverse the image for every 3x3 area
#find the median of pixels
#replace the center pixel by the median

img_new=np.zeros([m,n])

for i in range(1,m-1):
    for j in range(1,n-1):
        temp=[noisy[i-1,j-1],
             noisy[i-1,j],
             noisy[i-1,j+1],
             noisy[i,j-1],
             noisy[i,j],
             noisy[i,j+1],
             noisy[i+1,j-1],
             noisy[i+1,j],
             noisy[i+1,j+1],]
        temp=sorted(temp)
        img_new[i,j]=temp[4]

img_new=img_new.astype(np.uint8)
cv2.imshow('original',noisy)
cv2.imshow('final',img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()