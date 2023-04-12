import cv2
import numpy as np

img = cv2.imread('../data/H.png', 0)

binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

kernel = np.ones((5, 5), np.uint8)

invert = cv2.bitwise_not(binr)
for i in range(25):
    opening = cv2.morphologyEx(binr, cv2.MORPH_OPEN, kernel, iterations=i)
    cv2.imshow(f"after opening image iter={i}", opening)
    cv2.waitKey(100)

cv2.destroyAllWindows()
