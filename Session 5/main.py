import cv2
import os
import numpy as np

img = cv2.imread("Session 5/chessboard2.jpg")


#cv2.imshow("Image", img)
#cv2.waitKey(0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

harris = cv2.cornerHarris(gray_img, 2, 3, 0.04)
#cv2.imshow("Harris", harris)
#cv2.waitKey(0)

harris_img = img.copy()
harris_img[harris > 0.01 * harris.max()] = [0, 0, 225]
#cv2.imshow("Harris", harris)
#cv2.waitKey(0)

_, thres = cv2.threshold(harris, 0.01*harris.max(), 255, cv2.THRESH_BINARY)
_, _, _, centriods = cv2.connectedComponentsWithStats(np.uint8(thres))
criteria = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 100, 0.001)

corner_subpix = cv2.cornerSubPix(gray_img, np.float32(centriods), (5, 5), (-1, -1), criteria)


subpix_img=img.copy()
for corner in corner_subpix:
    corner_x = int(corner[0])
    corner_y = int(corner[1])
    subpix_img[corner_y, corner_x] = [0, 255, 0]

#cv2.imshow('subpix', subpix_img)
#cv2.waitKey(0)

import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
for i, file in enumerate(os.listdir("Session 5/images")):
    image = cv2.imread("Session 5/images/" + file)
    fast = cv2.FastFeatureDetector_create()
    orb = cv2.ORB_create()
    fast_kp = fast.detect(image)
    orb_kp = orb.detect(image)

    fast_img = image.copy()
    orb_img = image.copy()
    cv2.drawKeypoints(fast_img, fast_kp, fast_img, color=(255, 0, 0))
    cv2.drawKeypoints(orb_img, orb_kp, orb_img, color=(0, 0, 255))

    plt.subplot(3, 2, (i*2) + 1) #1 3 5
    plt.imshow(fast_img)

    plt.subplot(3, 2, (i*2) + 2) #2 4 6
    plt.imshow(orb_img)
plt.show()
