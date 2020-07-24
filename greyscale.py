import numpy as np
import cv2
from PIL import Image
from matplotlib import pyplot as plt

img = cv2.imread('original.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = Image.open('original.jpg').convert('LA') # or .convert('L')

plt.figure(num='NO BAYER FILTER - Failure')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gray),plt.title('Greyscale')
plt.xticks([]), plt.yticks([])
plt.show()
