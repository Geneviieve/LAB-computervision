import cv2
import matplotlib.pyplot as plt
import numpy as np

img  = cv2.imread("image.jpg", 0)
#cv2.imshow("image", img)
#cv2.waitKey(0)


gx = cv2.Sobel(img, cv2.CV_16S, 1, 0)
gy = cv2.Sobel(img, cv2.CV_16S, 0, 1)

#plt.figure(figsize=(8, 6))
#plt.subplot(1, 2, 1)
#plt.imshow(gx, 'gray')
#plt.title('Sobel X')
#plt.subplot(1, 2, 2)
#plt.imshow(gy, 'gray')
#plt.title('Sobel Y')
#plt.show()

#normalisasi

gx_abs = cv2.convertScaleAbs(gx)
gy_abs = cv2.convertScaleAbs(gy)

# res = np.sqrt(gx_abs**2 + gy_abs**2)
#res = cv2.addWeighted(gx_abs, 0.5, gy_abs, 0.5, 0)
#resized = cv2.resize(res, (256, 256))
#cv2.imshow('sobel', resized)
#cv2.waitKey(0)

###laplacian

#res = cv2.Laplacian(img, cv2.CV_8U)
#resized = cv2.resize(res, (512, 512))
#cv2.imshow('laplace', resized)
#cv2.waitKey(0)

#smoothing -> gaussian blur
#gradient magnitude kayak sobel
#non maximum suppression
#thresholding -> edge kuat (threshold sendiri), edge lemah (threshold sendiri), non edge
#konemsiin edge lemah dan kuat tapi dengan constrain


###canny

res = cv2.Canny(img, 200, 100)
resized = cv2.resize(res, (512, 512))
cv2.imshow('canny', resized)
cv2.waitKey(0)