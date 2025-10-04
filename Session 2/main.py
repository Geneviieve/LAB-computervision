import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("1.jpg")
#cv2.imshow("test", img)
#cv2.waitKey(0)


#resize image (jadi setengahnya)
scale_factor = 0.5
original_shape = img.shape

fianl_width = int(original_shape[1]*scale_factor)
final_height = int(original_shape[0]*scale_factor)

final_dim = (fianl_width, final_height)
resized_image = cv2.resize(img, final_dim, cv2.INTER_AREA)

cv2.imshow("resized image:", resized_image)
cv2.waitKey(0)

## convert color 
# coba grayscale

grayscaled_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #ini banyak bisa diconvertnya ke macem" gitu
cv2.imshow("Grayscaled image:", grayscaled_image)
cv2.waitKey(0)

## plotting intensity values

height = img.shape[0]
width = img.shape[1]
intensity_counter = np.zeros(256, dtype=int)

for i in range (height):
    for j in range(width):
        intensity_counter[grayscaled_image[i][j]] +- 1

plt.plot(intensity_counter, "g", "Intensity Counter")
plt.legend(loc='upper right')
plt.xlabel("Intensity")
plt.ylabel("Quantity")
plt.show()


##Hisotogram equalization
# apply historgram equalization
equalize_image = cv2.equalizeHist(grayscaled_image)

# plot intensity values of histogram equalization

eq_intensity_counter = np.zeros(256, dtype=int)

for i in range (height):
    for j in range(width):
        eq_intensity_counter[equalize_image[i][j]] +- 1

plt.plot(eq_intensity_counter, "g", "Intensity Counter")
plt.legend(loc='upper right')
plt.xlabel("Intensity")
plt.ylabel("Quantity")
plt.show()


## visualization with subplot

plt.figure(1, 16, 8)
plt.subplot(1, 2, 1)
plt.plot(intensity_counter, 'g', label='Before')
plt.legend(loc='upper right')
plt.xlabel("Intensity")
plt.ylabel("Quantity")
plt.show()

plt.subplot(1, 2, 2)
plt.plot(eq_intensity_counter, 'g', label='After')
plt.legend(loc='upper right')
plt.xlabel("Intensity")
plt.ylabel("Quantity")
plt.show()

