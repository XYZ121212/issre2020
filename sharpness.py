from PIL import Image, ImageEnhance
from matplotlib import pyplot as plt

'''
Sharpness: This class can be used to adjust the sharpness
of an image. An enhancement factor of 0.0 gives a
blurred image, a factor of 1.0 gives the original
image, and a factor of 2.0 gives a sharpened image.
'''

img = Image.open("original.jpg")

enhancer = ImageEnhance.Sharpness(img)

factor = 1
img1 = enhancer.enhance(factor)

factor = -3.5
img2 = enhancer.enhance(factor)


plt.figure(num='SHARPNESS Failure')
plt.subplot(121),plt.imshow(img1),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img2),plt.title('Sharpness')
plt.xticks([]), plt.yticks([])
plt.show()
