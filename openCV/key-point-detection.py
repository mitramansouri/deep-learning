import cv2
import matplotlib.pyplot as plt
# Our goal is to find  corners, blobs, or edges
# Load the image in grayscale
img = cv2.imread("sample.jpg", cv2.IMREAD_GRAYSCALE)

# Initialize ORB detector
orb = cv2.ORB_create()

# Detect keypoints and descriptors
keypoints, descriptors = orb.detectAndCompute(img, None)

# Draw keypoints on the image
img_with_kp = cv2.drawKeypoints(img, keypoints, None, color=(0,255,0), flags=0)

# Show the result
plt.figure(figsize=(10, 5))
plt.imshow(img_with_kp, cmap="gray")
plt.title(f"ORB Keypoints (found {len(keypoints)})")
plt.axis("off")
plt.show()

# Open a video file (replace 'video.mp4' with your file)
video = cv2.VideoCapture("driver-action-recognition.mp4")

# Check if the video loaded correctly
if not video.isOpened():
    print("Error: Could not open video file.")
else:
    print("Video loaded successfully!")

# Read and display the video frame by frame

while True:
    ret, frame = video.read()  # Read the next frame
    if not ret:
        break  # Stop if the video ends
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    # Initialize ORB detector
    orb = cv2.ORB_create()

    # Detect keypoints and descriptors
    keypoints, descriptors = orb.detectAndCompute(equalized, None)

    # Draw keypoints on the image
    frame_with_kp = cv2.drawKeypoints(equalized, keypoints, None, color=(0,255,0), flags=0)

    cv2.imshow("Video Playback", frame_with_kp)  # Show the frame

    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

cv2.destroyAllWindows()
