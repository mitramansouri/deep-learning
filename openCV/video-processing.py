import cv2
#  you can find the sample vidoes at "https://github.com/intel-iot-devkit/sample-videos?tab=readme-ov-file"
# Open a video file (replace 'video.mp4' with your file)
video = cv2.VideoCapture("driver-action-recognition.mp4")
# Create and save a video 
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output-blurred.mp4", fourcc, 30, (640, 480), isColor=False)

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

    cv2.imshow("Video Playback", frame)  # Show the frame

    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

video.release()
cv2.destroyAllWindows()
# Capture Video from a Webcam
camera = cv2.VideoCapture(0)  # 0 = Default webcam
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

    cv2.imshow("Video Playback", frame)  # Show the frame

    # Press 'q' to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        # If no key is pressed, it waits for 25 mili seconds.
        # If any key is pressed, it immediately stops waiting and moves to the next frame.
        break

video.release()
cv2.destroyAllWindows()


# Convert video to grayscale 
video = cv2.VideoCapture("driver-action-recognition.mp4")

while True:
    ret, frame = video.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    cv2.imshow("Grayscale Video", gray_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

# Blurre a video 
video = cv2.VideoCapture("driver-action-recognition.mp4")

while True:
    ret, frame = video.read()
    if not ret:
        break

    blurred = cv2.GaussianBlur(frame, (15, 15), 120)
    cv2.imshow("Grayscale Video", blurred)
    out.write(blurred) 

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
out.release()  # Save and close the video file
cv2.destroyAllWindows()
