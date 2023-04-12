import cv2
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set_style('darkgrid')
colors = ["#ffbe0b", "#fb5607", "#ff006e", "#8338ec", "#3a86ff"]
rgb = ["#118ab2", "#06d6a0", "#ef476f"]

# reading image from data/ folder using opencv
lena_image = cv2.imread('Practical 1\data\lena.png', 1)
lena_image_bw = cv2.imread('Practical 2\data\cameraman.jpg')
# cv2.imshow("Lena Image", lena_image)

plt.figure(figsize=(20, 10))
for i, col in enumerate(['blue', 'green', 'red']):
    histogram = cv2.calcHist([lena_image], [i], None, [256], [0, 256])
    plt.subplot(1, 3, i + 1)
    plt.title(col)
    plt.plot(histogram, color=rgb[i])

histogram_bw = cv2.calcHist([lena_image_bw], [0], None, [256], [0, 256])

# plt.figure(figsize=(20, 10))
# plt.subplot(221)
# plt.title('Image Histogram')
# plt.xlabel('bins')
# plt.ylabel('No. of Pixels')
# plt.hist(histogram, color=colors[0])
#
# plt.subplot(222)
# plt.title('Image Plot')
# plt.xlabel('bins')
# plt.ylabel('No. of Pixels')
# plt.plot(histogram, color=colors[1])

# plt.subplot(223)
# plt.title('Image Histogram B/W')
# plt.xlabel('bins')
# plt.ylabel('No. of Pixels')
# plt.hist(histogram_bw, color=colors[3])
#
# plt.subplot(224)
# plt.title('Image Plot B/W')
# plt.xlabel('bins')
# plt.ylabel('No. of Pixels')
# plt.plot(histogram_bw, color=colors[4])
# plt.savefig('../plots/hist_rgb.svg', dpi=350)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = cv2.imread("Practical 2\data\cameraman.jpg",0) 
equ =cv2.equalizeHist(img3) 
res = np.hstack((img3,equ)) 
cv2.imshow('image',res) 
histr1 = cv2.calcHist([img3],[0],None,[256],[0,256]) 
histr2 = cv2.calcHist([equ],[0],None,[256],[0,256]) 
plt.plot(histr1) 
plt.plot(histr2) 
plt.show() 
plt.subplot(1,2,1) 
plt.title("Original")
plt.imshow(img3)