import cv2
import matplotlib.pyplot as plt
img_bgr = cv2.imread('mosque.jpeg', 1)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img_bgr], 
                         [i], None,
                         [256], 
                         [0, 256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
plt.show()
height, width, _ = img_bgr.shape
for i in range(0, height - 1):
    for j in range(0, width - 1):
        pixel = img_bgr[i, j]
        pixel[0] = 255 - pixel[0]
        pixel[1] = 255 - pixel[1]
        pixel[2] = 255 - pixel[2]
        img_bgr[i, j] = pixel
plt.imshow(img_bgr)
cv2.imwrite('negative.jpg', img_bgr)
plt.show()
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img_bgr], 
                         [i], None,
                         [256],
                         [0, 256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])
plt.show()