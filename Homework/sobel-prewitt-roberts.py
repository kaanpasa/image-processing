import numpy as np
from scipy import ndimage

img = cv2.imread('mosque.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)


#sobel
img_sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
img_sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
img_sobel = img_sobelx + img_sobely


#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)

#Robert's Cross
roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )
  
img = cv2.imread("mosque.jpeg",0).astype('float64')
img/=255.0
vertical = ndimage.convolve( img, roberts_cross_v )
horizontal = ndimage.convolve( img, roberts_cross_h )
  
roberts_cross = np.sqrt( np.square(horizontal) + np.square(vertical))
roberts_cross*=255



cv2.imshow("Original Image", img)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)
cv2.imshow("Robert's Cross", roberts_cross)


cv2.waitKey(0)
cv2.destroyAllWindows()