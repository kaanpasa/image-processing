import cv2
import numpy as np
import matplotlib.pyplot as plt
   

image = cv2.imread('mosque.jpeg')
   

c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

log_image = np.array(log_image, dtype = np.uint8)
   
cv2.imwrite('log_image.jpg', log_image)