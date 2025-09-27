import cv2
import numpy as np

image = cv2.imread("picture.jpg")
cv2.imshow(image)

#buat close window kalo usernya press sembuah key
cv2.waitKey(0)

print(image) #kalo ini gambarnya dbaca dalam sebuah array yang isinya intensity values dari setiap color value

print(np.shape(image)) #ini outputnya (size y, size x, intensity value dari setiap color valuenya (kalo 3 berarti berwarn, kalo 2 biasanya b&w))


#jadi disini kita ngilangin value warna biru
image[:, :, 0] = 0 #bikin intensitas birunya 0
image[:, :, 1] = 0 #bikin intensitas ijonya 0

cv2.imshow("Manipulated image:", image)
cv2. waitKey(0)

#jadi dia udh gapunya value ijo sama ibur, sisanya merah doang
image[:, :, 2] = 0 #bikin intensitas merahnya 0
#jadi gambarnya item

cv2.imshow("Manipulated image:", image)
cv2. waitKey(0)


image[:, 100:230, 0] = 0 #modify pixel tertentunya
image[:, :, 1] = 0 #bikin intensitas ijonya 0


cv2.imshow("Manipulated image:", image)
cv2. waitKey(0)

cv2.imwrite("processed_image.jpg", image)