import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np 

# 1 Image proccessing 
# Write a Python program that:
# Loads an image (sample.jpg).
img = cv.imread("sample.jpg")
# Converts it to grayscale and displays it.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Applies Gaussian Blur with a kernel size of (7,7) and displays the result.
blurred = cv.GaussianBlur(img, (7, 7), 0)
# Applies Canny Edge Detection with threshold1=50 and threshold2=150.
edge = cv.Canny(img,50,150)
# Displays all processed images using Matplotlib in a single figure (subplot format).
plt.figure(figsize=(10,5))
plt.subplot(1,4,1)
plt.imshow(img)
plt.title("Image")
plt.axis("off")
plt.subplot(1,4,2)
plt.imshow(blurred)
plt.title("Blurred")
plt.axis("off")
plt.subplot(1,4,3)
plt.imshow(gray, cmap='gray')
plt.title("Gray")
plt.axis("off")
plt.subplot(1,4,4)
plt.imshow(edge, cmap='gray')
plt.title("Edge")
plt.axis("off")
plt.show()
# 1 Image proccessing 
# Write a Python program that:
# Loads an image (sample.jpg).
img = cv.imread("sample.jpg")
# Converts it to grayscale and displays it.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Applies Gaussian Blur with a kernel size of (7,7) and displays the result.
blurred = cv.GaussianBlur(img, (7, 7), 0)
# Applies Canny Edge Detection with threshold1=50 and threshold2=150.
edge = cv.Canny(img,50,150)
# Displays all processed images using Matplotlib in a single figure (subplot format).
plt.figure(figsize=(10,5))
plt.subplot(1,4,1)
plt.imshow(img)
plt.title("Image")
plt.axis("off")
plt.subplot(1,4,2)
plt.imshow(blurred)
plt.title("Blurred")
plt.axis("off")
plt.subplot(1,4,3)
plt.imshow(gray, cmap='gray')
plt.title("Gray")
plt.axis("off")
plt.subplot(1,4,4)
plt.imshow(edge, cmap='gray')
plt.title("Edge")
plt.axis("off")
plt.show()
