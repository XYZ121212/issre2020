from PIL import Image
from numpy import*
import cv2
from matplotlib import pyplot as plt

# Open image and put it in a numpy array
srcArray = cv2.imread('original.jpg')
srcArray1 = Image.open("original.jpg")

w, h, _ = srcArray.shape
# Create target array, twice the size of the original image
resArray = zeros((2*w, 2*h, 3), dtype=uint8)

# Map the RGB values in the original picture according to the BGGR pattern#

# Blue
resArray[::2, ::2, 2] = srcArray[:, :, 2]

# Green (top row of the Bayer matrix)
resArray[1::2, ::2, 1] = srcArray[:, :, 1]

# Green (bottom row of the Bayer matrix)
resArray[::2, 1::2, 1] = srcArray[:, :, 1]

# Red
resArray[1::2, 1::2, 0] = srcArray[:, :, 0]

resArray = cv2.cvtColor(resArray, cv2.COLOR_BGR2RGB)
# Save the image
imgOut = Image.fromarray(resArray, "RGB")
#imgOut = imgOut.resize((h,w), Image.ANTIALIAS)
# Save the image
# imgOut.save("nodemos.png")

plt.figure(num='NO DEMOSAICING Failure')
plt.subplot(121),plt.imshow(srcArray1),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imgOut),plt.title('No Demosaicing')
plt.xticks([]), plt.yticks([])
plt.show()
