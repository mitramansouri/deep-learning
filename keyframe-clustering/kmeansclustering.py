import cv2 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

cap = cv2.VideoCapture("sample.mp4")

# Check if the video loaded correctly
if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    print("Video loaded successfully!")
frames = []
features = []
frame_indices = []
interval = 30
i = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if i % interval == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness = np.mean(gray)
        features.append([brightness])
        frame_indices.append(i)
    i += 1

cap.release()

# Step 3: Run k-Means clustering
k = 3
kmeans = KMeans(n_clusters=k, random_state=0).fit(features)
labels = kmeans.labels_

# Step 4: Plot the clustering
features = np.array(features)
plt.figure(figsize=(10, 5))
for cluster in range(k):
    cluster_points = features[labels == cluster]
    frame_ids = np.array(frame_indices)[labels == cluster]
    plt.scatter(frame_ids, cluster_points, label=f'Cluster {cluster}')

plt.title('Frame Clustering by Brightness')
plt.xlabel('Frame Index')
plt.ylabel('Average Brightness')
plt.legend()
plt.grid(True)
plt.show()