import numpy as np
import cv2
from matplotlib import pyplot as plt
import random

img = cv2.imread('original.jpg')

img1 = cv2.imread('original.jpg')

h, w, _ = img1.shape

count = 0
w1 = w2 = int((w-70)/10)
h1 = h2 = int((h-70)/5)
w2 = w3 = w2 - 5
h2 = h3 = h2 - 5
countpixel = 0


for y in range(0, 5):
    h2 = h2 + (h1*y)
    for x in range(0, 10):
        img1[h2,w2] = (255, 0, 0)
        countpixel = countpixel + 1
        w2 = w2 + w1
        if x==9:
            h2 = h3
            w2 = w3


print(countpixel)

plt.figure(num='DEADPIXEL Failure - Configuration 2')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img1),plt.title('DEADPIXEL - Configuration 2')
plt.xticks([]), plt.yticks([])
plt.show()
