import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np 

# Video Processing & Object Detection
# Capture video from the webcam using OpenCV.
camera = cv.VideoCapture(0)  # 0 = Default webcam
# Check if the video loaded correctly
if not camera.isOpened():
    print("Error: Could not open video file.")
else:
    print("Video loaded successfully!")

# Read and display the video frame by frame

while True:
    ret, frame = camera.read()  # Read the next frame
    if not ret:
        break  # Stop if the video ends

    cv.imshow("Video Playback", frame)  # Show the frame

    # Press 'q' to exit
    if cv.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

cv.destroyAllWindows()
# Convert each frame to grayscale and display it.
while True:
    ret, frame = camera.read()  # Read the next frame
    if not ret:
        break  # Stop if the video ends

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video Playback", gray)  # Show the frame

    # Press 'q' to exit
    if cv.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

cv.destroyAllWindows()
# Apply Canny Edge Detection on the video feed.
while True:
    ret, frame = camera.read()  # Read the next frame
    if not ret:
        break  # Stop if the video ends

    canny = cv.Canny(frame,100,150)
    cv.imshow("Video Playback", canny)  # Show the frame

    # Press 'q' to exit
    if cv.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

cv.destroyAllWindows()

#  Video Processing & Object Detection
# Capture video from the webcam using OpenCV.
camera = cv.VideoCapture(0)  # 0 = Default webcam
# Check if the video loaded correctly
if not camera.isOpened():
    print("Error: Could not open video file.")
else:
    print("Video loaded successfully!")

# Read and display the video frame by frame

while True:
    ret, frame = camera.read()  # Read the next frame
    if not ret:
        break  # Stop if the video ends

    cv.imshow("Video Playback", frame)  # Show the frame

    # Press 'q' to exit
    if cv.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

cv.destroyAllWindows()
# Convert each frame to grayscale and display it.
while True:
    ret, frame = camera.read()  # Read the next frame
    if not ret:
        break  # Stop if the video ends

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Video Playback", gray)  # Show the frame

    # Press 'q' to exit
    if cv.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

cv.destroyAllWindows()
# Apply Canny Edge Detection on the video feed.
while True:
    ret, frame = camera.read()  # Read the next frame
    if not ret:
        break  # Stop if the video ends

    canny = cv.Canny(frame,100,150)
    cv.imshow("Video Playback", canny)  # Show the frame

    # Press 'q' to exit
    if cv.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

cv.destroyAllWindows()
