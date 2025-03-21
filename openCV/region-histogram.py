import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image and convert to grayscale
img = cv2.imread("sample.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a blank mask (same size as grayscale image)
mask = np.zeros(gray.shape, dtype="uint8")

# Define and draw a filled white rectangle (ROI) on the mask
cv2.rectangle(mask, (50, 50), (200, 200), 255, -1)  # x1,y1 to x2,y2

# Apply the mask using bitwise AND
masked_region = cv2.bitwise_and(gray, gray, mask=mask)

# Calculate histograms
full_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
masked_hist = cv2.calcHist([gray], [0], mask, [256], [0, 256])

# Plot everything
plt.figure(figsize=(12, 6))

# Show mask and masked image
plt.subplot(2, 2, 1)
plt.imshow(mask, cmap="gray")
plt.title("Mask")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(masked_region, cmap="gray")
plt.title("Masked Region")
plt.axis("off")

# Histograms
plt.subplot(2, 2, 3)
plt.plot(full_hist, label="Full Image", color="gray")
plt.plot(masked_hist, label="Masked Region", color="red")
plt.title("Histogram Comparison")
plt.xlabel("Pixel Intensity")
plt.ylabel("Pixel Count")
plt.legend()

plt.tight_layout()
plt.show()
