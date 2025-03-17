import cv2

# Read a JPG and show it 
img = cv2.imread("sample.jpg")
cv2.imshow("Original IMG" , img)
cv2.waitKey(0)  
cv2.destroyAllWindows()

# Applying edge detection 
edges_low = cv2.Canny(img,50,150)
edges = cv2.Canny(img,100,200)
edges_high = cv2.Canny(img,250,300)
edges_high_range = cv2.Canny(img,20,300)
edges_low_range = cv2.Canny(img,250,270)
# cv2.Canny(image, threshold1, threshold2)
# threshold1 (100) → Lower threshold: Determines which edges are weak.
# threshold2 (200) → Upper threshold: Strong edges must be above this.
# Lower values → More edges (including weak ones, more noise).
# Higher values → Fewer edges (only the strongest edges remain).
cv2.imshow("Filtered with canny low", edges_low)
cv2.imshow("Filtered with canny", edges)
cv2.imshow("Filtered with canny high", edges_high)
# Valid Threshold Ranges:
# Min: cv2.Canny(image, 0, 255) (detects almost everything, including noise)
# Max: cv2.Canny(image, 255, 255) (detects almost nothing)
cv2.imshow("Filtered with canny high", edges_high_range)
cv2.imshow("Filtered with canny low", edges_low_range)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying Gaussian Blur
blurred = cv2.GaussianBlur(img, (15, 15), 120)
# (15,15) is the kernel size (larger values = more blur)
# First value (15) → Width of the filter (kernel size in X direction)
# Second value (15) → Height of the filter (kernel size in Y direction)
# The third value is sigmaX, which is the standard deviation in the X direction.
# If 0 is given, OpenCV automatically calculates the best value based on the kernel size.
# Higher sigma = stronger blur
cv2.imshow("Filtered with Gaussian", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying the grayscale 
# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
