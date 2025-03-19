import cv2
import numpy as np
import matplotlib.pyplot as plt
# # It tells us how many pixels have a certain brightness level.
# Helps us understand the contrast, brightness, and exposure of an image.
# Used in image enhancement, segmentation, and feature extraction.
img = cv2.imread("sample.jpg")
cv2.imshow("Image", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", gray)
cv2.waitKey(0)  # Wait for key press
cv2.destroyAllWindows()  # Close the window


# Compute the histogram
hist_gray = cv2.calcHist([gray], [0], None, [16], [0, 256])
hist_blue = cv2.calcHist([img], [0], None, [16], [0, 256])
hist_green = cv2.calcHist([img], [1], None, [16], [0, 256])
hist_red = cv2.calcHist([img], [2], None, [16], [0, 256])
# [gray] The input image (must be in a list).
# [0] The channel (0 = grayscale, 0 = Blue, 1 = Green, 2 = Red). BGR scale
# None : Defines a specific region of the image for histogram calculation.
mask = np.zeros(img.shape[:2], dtype="uint8")  # Create a black mask
cv2.rectangle(mask, (50, 50), (200, 200), 255, -1)  # Draw a white rectangle

# Show the mask
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(mask, cmap="gray")
plt.title("Mask")
plt.axis("off")
# Apply the mask to the image
masked_img = cv2.bitwise_and(img, img, mask=mask)
# Show the masked image
plt.subplot(1,2,2)
plt.imshow(cv2.cvtColor(masked_img, cv2.COLOR_BGR2RGB))
plt.title("Masked Image")
plt.axis("off")
hist_masked = cv2.calcHist([masked_img], [0], None, [16], [0, 256])

plt.show()
# Plot the histogram
plt.figure()
plt.title("Histogram")
plt.xlabel("Pixel Value (0-15)")
plt.ylabel("Frequency")
plt.plot(hist_gray, color='gray')
plt.plot(hist_blue, color='blue')
plt.plot(hist_blue, color='blue')
plt.plot(hist_masked,color='yellow')
plt.plot(hist_red, color='red')
plt.xlim([0, 16])
plt.show()
