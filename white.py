from PIL import Image
from matplotlib import pyplot as plt

picture1 = Image.open("original.jpg")
picture = Image.open("original.jpg")

pixels = picture.load()
width, height = picture.size

for i in range(0,width):
    for j in range(0,height):
        pixels[i,j] = (255, 255, 255)


plt.figure(num='WHITE Failure')
plt.subplot(121),plt.imshow(picture1),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(picture),plt.title('White')
plt.xticks([]), plt.yticks([])
plt.show()
