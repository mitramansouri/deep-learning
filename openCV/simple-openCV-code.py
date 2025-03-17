import cv2
print("OpenCV Version:", cv2.__version__)


# Load the image
img = cv2.imread("sample.jpg")

# Check if the image loaded correctly
if img is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully!")


# Display the image
cv2.imshow("Loaded Image", img)  
print("Image size H X W",img.shape[0] , img.shape[1])
print("Image channels", img.shape[2])
# Resize the image
small = cv2.resize(src=img, dsize=(180, 120))
cv2.imshow("Small", small)
cv2.waitKey(0)  # Wait for key press
cv2.destroyAllWindows()  # Close the window

# Convert BGR to RGB for correct colors
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# optional second parameter:
 #-1 (default): cv.IMREAD_COLOR - color but ignores transparency
 #0: cv.IMREAD_GRAYSCALE - only grayscaled
 #1: cv.IMREAD_UNCHANGED - with transparency
img2 = cv2.imread("sample.jpg",0)
cv2.imshow("Grayscale", img2)
cv2.waitKey(0)  # Wait for key press

#  copy part of image (i.e., of array)
center = img[100:250, 250:400]
cv2.imshow("Center-Copy", center)
cv2.imshow("Image", img)
cv2.waitKey(0)  # Wait for key press

