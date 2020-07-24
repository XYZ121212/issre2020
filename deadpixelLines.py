import numpy as np
import cv2
from matplotlib import pyplot as plt
import random
from PIL import Image

img = Image.open('original.jpg')

img1 = Image.open('original.jpg')
pixels = img1.load()
width, height = img1.size

#horizontal
for i in range(0,width):
    for j in range(0,height):
        if i==120 and j==50:
            for k in range(0,20):
                pixels[i+k,j] = (0,0,0)

#vertical
for i in range(0,width):
    for j in range(0,height):
        if i==125 and j==20:
            for k in range(0,35):
                pixels[i,j+k] = (0,0,0)

#oblique to the right
count = 0
for i in range(0,width):
    for j in range(0,height):
        if i>=225 and i<=(225+count) and j>100 and count<45:
            pixels[i,j] = (0,0,0)
            count = count + 1
            i = i + 1

#obstacle simulation
for i in range(0,width):
    for j in range(0,height):
        if i==177 and j==120:
            for p in range(0,10):
                for k in range(0,46):
                    pixels[i+k,j+p] = (0,0,0)

img1 = np.array(img1)

plt.figure(num='DEADPIXEL Failure Configuration 6 - 7 - 8 - 9')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img1),plt.title('DEADPIXEL - Configuration 6 - 7 - 8 - 9')
plt.xticks([]), plt.yticks([])
plt.show()
