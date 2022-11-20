import cv2
import numpy as np
image = cv2.imread('blur1.png')
kernel = np.array([[0, -1, 0],
                   [-1, 5.2,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
cv2.imwrite('sharp2.jpg', image_sharp)