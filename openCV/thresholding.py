import cv2
import matplotlib.pyplot as plt

# Load a grayscale image
img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

# Apply binary thresholding
threshold_value = 127
max_value = 255
_, thresh = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)

# Show original and thresholded image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(thresh, cmap="gray")
plt.title(f"Binary Threshold (T = {threshold_value})")
plt.axis("off")

plt.tight_layout()
plt.show()
