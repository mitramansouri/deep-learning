import cv2
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram


# Loading the video
video = cv2.VideoCapture("sample.mp4")

# Checking to see if the video loaded correctly
if not video.isOpened():
    print("Error: Could not open video file.")
else:
    print("Video loaded successfully!")

# Extracting the keyframes 
interval = 60  # extract every 60th frame
frame_index = 0
keyframes = []
histograms = []

while True:
    ret, frame = video.read()
    if not ret:
        break

    if frame_index % interval == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([gray], [0], None, [32], [0, 256])
        histograms.append(hist.flatten())
        keyframes.append(frame)

    frame_index += 1

video.release()

print(f"Extracted {len(keyframes)} keyframes.")


# Clustering using average-linkage 
linked = linkage(histograms, method='average')

# Showing dendrogram 
plt.figure(figsize=(10, 4))
dendrogram(linked, labels=[f"KF{i}" for i in range(len(keyframes))])
plt.title("Keyframe Clustering (Color Histogram, Average Linkage)")
plt.xlabel("Keyframe")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()