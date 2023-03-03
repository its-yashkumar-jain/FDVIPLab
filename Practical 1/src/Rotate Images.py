import cv2
import numpy as np

# reading image from data/ folder using opencv
lena_image = cv2.imread('../data/lena.png', 1)
cv2.imshow("Lena Image", lena_image)

# Get shape (h, w, d) of the image that is read
[h, w, d] = lena_image.shape
print(f'Height of image : {h}\nWidth of image : {w}\nDepth of image : {d}')

# rotate 90 degrees clockwise
lena_image_90_clk = cv2.rotate(lena_image, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Lena Image 90 Clockwise", lena_image_90_clk)

# Get shape (h, w, d) of the image that is read
[h, w, d] = lena_image_90_clk.shape
print(f'Height of image : {h}\nWidth of image : {w}\nDepth of image : {d}')

lena_image_180 = cv2.rotate(lena_image, cv2.ROTATE_180)
cv2.imshow("Lena Image 180", lena_image_180)

# Get shape (h, w, d) of the image that is read
[h, w, d] = lena_image_180.shape
print(f'Height of image : {h}\nWidth of image : {w}\nDepth of image : {d}')

lena_image_270 = cv2.rotate(lena_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("Lena Image 180", lena_image_270)

# Get shape (h, w, d) of the image that is read
[h, w, d] = lena_image_270.shape
print(f'Height of image : {h}\nWidth of image : {w}\nDepth of image : {d}')

cv2.waitKey(0)
cv2.destroyAllWindows()
