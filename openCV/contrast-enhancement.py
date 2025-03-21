import cv2
import matplotlib.pyplot as plt

# Load a grayscale image (low-contrast)
img = cv2.imread("grayscale.jpg", cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
equalized = cv2.equalizeHist(img)

# Plot original and equalized images side by side
plt.figure(figsize=(12, 6))

# Original image and its histogram
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.hist(img.ravel(), bins=256, range=[0, 256])
plt.title("Original Histogram")

# Equalized image and its histogram
plt.subplot(2, 2, 3)
plt.imshow(equalized, cmap='gray')
plt.title("Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.hist(equalized.ravel(), bins=256, range=[0, 256])
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()
