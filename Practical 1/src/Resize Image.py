import cv2
import numpy as np

img = cv2.imread('../data/lena.png')

(height, width) = img.shape[0:2]

new_img = cv2.resize(img, (height - 200, width + 200))

cv2.imshow("Original Image", img)
cv2.imshow("New Image", new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
