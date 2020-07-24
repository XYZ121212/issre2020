import cv2
from matplotlib import pyplot as plt

img = cv2.imread('original.jpg')

blur = cv2.blur(img,(12,12))
#blur e img --> <class 'numpy.ndarray'>

plt.figure(num='BLURRED Failure')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
