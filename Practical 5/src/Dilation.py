import cv2
import numpy as np

img = cv2.imread('../data/mri_2.png', 0)

binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = np.ones((3, 3), np.uint8)

invert = cv2.bitwise_not(binr)

dilation = cv2.dilate(invert, kernel, iterations=1)

cv2.imshow("dilated image", dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
