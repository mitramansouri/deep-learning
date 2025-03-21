import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np 
# 3 Region-Based Histogram Analysis
# Load a grayscale image (gray_sample.jpg).
gray_sample = cv.imread("grayscale.jpg", cv.IMREAD_GRAYSCALE)
cv.imshow("Gray", gray_sample)
cv.waitKey(0)  # Wait for key press
cv.destroyAllWindows()  # Close the window
# Create a mask that selects only a rectangular region (50, 50) to (200, 200).
mask = np.zeros(gray_sample.shape[:2], dtype="uint8")  # Create a black mask
cv.rectangle(mask, (50, 50), (200, 200), 255, -1)  # Draw a white rectangle
# Compute the histogram for the masked region and plot it alongside the full-image histogram.
masked_img = cv.bitwise_and(gray_sample, gray_sample, mask=mask)
hist_masked_gray = cv.calcHist([masked_img], [0], None, [16], [0, 256])
hist_normal = cv.calcHist([gray_sample],[0] , None, [16], [0,256])
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(hist_masked_gray)
plt.title("Masked Gray Histogram")
plt.xlim([0, 16])
plt.subplot(2,2,2)
plt.plot(hist_normal)
plt.title("Normal Gray Histogram")
plt.xlim([0, 16])
plt.subplot(2,2,3)
plt.imshow(masked_img, cmap='gray')
plt.title("Masked Picture")
plt.subplot(2,2,4)
plt.imshow(gray_sample, cmap='gray')
plt.title("Gray picture")
plt.show()
# Compare the two histograms and discuss the differences.
