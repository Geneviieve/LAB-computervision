import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images.jpg")

#cv2.imshow("Image", img)
#cv2.waitKey(0)

## Grayscaling
#img_grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Image Grayscaled", img_grayscale)
#cv2.waitKey(0)

######################

#img = cv2.imread("images.jpg", 0) #flag 0 -> auto grayscale

#cv2.imshow("Image Grayscaled", img)
#cv2.waitKey(0)

# tresholding
# A. binary - mau set jadi 0 ato 1, putih ato hitam berdasarkan threshold, gaada abu"

#_, img_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
#cv2.imshow("Image Binary", img_binary)
#cv2.waitKey(0)


# B. binary Inverse - kebalikannya(0-> putih, 1 -> hitam)

#_, img_binary_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#cv2.imshow("Image Binary", img_binary_inv)
#cv2.waitKey(0)


# C. Tozero - hitam, atau originalnya sampai threshold tertentu

#_, img_tozero = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
#cv2.imshow("Image Binary", img_tozero)
#cv2.waitKey(0)

# D. Tozero Inverse - kalo lebih besar dari threshold dibikin jadi 0

#_, img_tozero_inv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
#cv2.imshow("Image Binary", img_tozero_inv)
#cv2.waitKey(0)

# E. Trunc - kasih limit ke setiap pixel value jadi 127

#_, img_trunc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
#cv2.imshow("Image Binary", img_trunc)
#cv2.waitKey(0)


# F. OTSU - bikin dia set optimal threshold

#_, img_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
#cv2.imshow("Image Binary", img_otsu)
#cv2.waitKey(0)

#### plotting
#result_images = [
#    img_binary, img_binary_inv, img_tozero, img_tozero_inv, img_trunc, img_otsu ]

#titles = [
#    "image binary", "image binary inverse", "image tozero", "image tozero inverse", "image trunc", "image otsu"]

#for index, (title, image) in enumerate(zip(titles, result_images)):
#    plt.subplot(2, 3, index +1)
#    plt.imshow(image, "gray")
#    plt.title(title)
    
#plt.show()


#### filtering
#a. Mean - satu piel bakal jadi mean dari pizel sekelilingnya
img_mean = cv2.blur(img, (11, 11))
#b. Median
img_median = cv2.medianBlur(img, 11)

#c. Gaussian
img_gaussian = cv2.GaussianBlur(img, (11, 11), 0) #0 ini standard deviation

#d. Bilateral
img_bilateral = cv2.bilateralFilter(img, 11, 120, 120)


#### plotting
result_images = [
    img_mean, img_median, img_gaussian, img_bilateral]

titles = [
    "image mean", "image median", "image gaussian", "image bilateral filter"]

for index, (title, image) in enumerate(zip(titles, result_images)):
    plt.subplot(1, 4, index +1)
    plt.imshow(image, "gray")
    plt.title(title)
    
plt.show()
