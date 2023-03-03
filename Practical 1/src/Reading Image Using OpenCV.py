import cv2
import numpy as np

# reading image from data/ folder using opencv
lena_image = cv2.imread('../data/lena.png', 1)
cv2.imshow("Lena Image", lena_image)
# print(lena_image)

# reading image from data/ folder using opencv with flag : 0 -> read grayscale, 1 -> color image
lena_image_gray = cv2.imread('../data/lena.png', 0)
cv2.imshow("Lena Image Gray", lena_image_gray)

# Get shape (h, w, d) of the image that is read
[h, w, d] = lena_image.shape
print(f'Height of image : {h}\nWidth of image : {w}\nDepth of image : {d}')

cv2.imwrite('../data/lena saved.jpg', lena_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
