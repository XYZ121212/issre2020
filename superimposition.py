from matplotlib import pyplot as plt
from PIL import Image


img = Image.open("original.jpg")

img2 = Image.open("broken1.png").convert(img.mode)

img2 = img2.resize(img.size)

img3 = Image.blend(img,img2,0.35)

plt.figure(num='BROKEN LENS Failure')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img3),plt.title('Broken Lens')
plt.xticks([]), plt.yticks([])
plt.show()
