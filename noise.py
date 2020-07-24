import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('original.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


gauss = np.random.normal(0,1,img.size)
gauss = gauss.reshape(img.shape[0],img.shape[1],img.shape[2]).astype('uint8')
noise = img + img * gauss

plt.figure(num='NOISE Failure')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(noise),plt.title('Noise')
plt.xticks([]), plt.yticks([])
plt.show()

#ok
