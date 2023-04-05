import cv2
import numpy as np

bw_image = cv2.imread("data/cameraman.jpg")
cv2.imshow("BW", bw_image)

gamma = 0.0
while gamma < 3.2:
    gamma_image = np.array(255 * (bw_image / 255) ** gamma, dtype=np.uint8)
    cv2.imshow("BW Power Log", gamma_image)

    cv2.waitKey(500)
    gamma += 0.1
cv2.destroyAllWindows()
