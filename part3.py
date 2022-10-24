"""
import cv2
import numpy as np

resim1 = cv2.imread("jameswebb.jpg")

cv2.imshow("James Webb Space Telescope", resim1)

print(resim1.size)

print(resim1.dtype)

print(resim1.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
########################################
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

row = 256
col = 256
img = np.zeros((row,col))
img[100:105, :] = 0.5
img[:, 100:105] = 1
plt.figure(figsize=(10,4))
plt.imshow(img)
plt.show()
"""
#########################################
import cv2
import numpy as np 

height = 512
width = 512
img = np.random.randint(255, size=(height, width, 1), dtype=np.uint8)

cv2.imshow('Binary',img)
cv2.waitKey(0)