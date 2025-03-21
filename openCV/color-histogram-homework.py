import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np 
# 2 Color Histogram Analysis
# Load a color image (color_sample.jpg).
color_img = cv.imread("sample.jpg")
# Compute and plot three separate histograms (Blue, Green, Red channels).
# Write a function that normalizes each histogram (divides by the total number of pixels).
def normalize_hist(hist_list):
    maximum = np.max(hist_list)
    normalized_hist_list = np.array([])
    normalized_hist_list = hist_list / maximum
    return normalized_hist_list

hist_blue = cv.calcHist([img], [0], None, [16], [0, 256])
hist_green = cv.calcHist([img], [1], None, [16], [0, 256])
hist_red = cv.calcHist([img], [2], None, [16], [0, 256])
normalized_blue = normalize_hist(hist_blue)
normalized_green = normalize_hist(hist_green)
normalized_red = normalize_hist(hist_red)

plt.figure(figsize=(15,10))
plt.subplot(2,3,1)
plt.plot(hist_blue)
plt.title("Blue Histogram")
plt.xlim([0, 16])
plt.subplot(2,3,2)
plt.plot(hist_green, color='green')
plt.title("Green Histogram")
plt.xlim([0, 16])
plt.subplot(2,3,3)
plt.plot(hist_red, color='red')
plt.title("Red Histogram")
plt.xlim([0, 16])
plt.subplot(2,3,4)
plt.plot(normalized_blue)
plt.title("Blue Histogram - Normalized")
plt.xlim([0, 16])
plt.subplot(2,3,5)
plt.plot(normalized_green, color='green')
plt.title("Green Histogram - Normalized")
plt.xlim([0, 16])
plt.subplot(2,3,6)
plt.plot(normalized_red, color='red')
plt.title("Red Histogram - Normalized")
plt.xlim([0, 16])
plt.show()
# Display the histograms in one plot, using:
# Blue for Blue Channel
# Green for Green Channel
# Red for Red Channel
plt.figure()
plt.title("Histogram")
plt.xlabel("Pixel Value (0-15)")
plt.ylabel("Frequency")
plt.plot(hist_blue, color='blue')
plt.plot(hist_green, color='green')
plt.plot(hist_red, color='red')
plt.xlim([0, 16])
plt.show()
