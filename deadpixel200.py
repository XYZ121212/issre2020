import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
from PIL import Image

img = Image.open('original.jpg')

img1 = cv2.imread('original.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

h, w, _ = img1.shape
print('width: ', w)
print('height:', h)

count = 0
w1 = w2 = int(w/20)
h1 = h2 = int(h/10)
w2 = w3 = w2 - 5
h2 = h3 = h2 - 5
countpixel = 0

for y in range(0, 10):
    h2 = h2 + (h1*y)
    for x in range(0, 20):
        img1[h2,w2] = (255, 0, 0)
        countpixel = countpixel + 1
        w2 = w2 + w1
        if x==19:
            h2 = h3
            w2 = w3

img1 = Image.fromarray(img1) #conversion

print(countpixel)

plt.figure(num='DEADPIXEL Failure - Configuration 3')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img1),plt.title('DEADPIXEL - Configuration 3')
plt.xticks([]), plt.yticks([])
plt.show()
