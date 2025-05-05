import cv2
import numpy as np
import torch
import torchvision.models as models
import torchvision.transforms as transforms
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import urllib.request
import os

# --- Step 0: Download ImageNet class labels (only once) ---
url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
label_file = "imagenet_classes.txt"
if not os.path.exists(label_file):
    urllib.request.urlretrieve(url, label_file)

with open(label_file, "r") as f:
    labels = [line.strip() for line in f.readlines()]

# --- Load pretrained ResNet18 (with final layer) ---
model = models.resnet18(pretrained=True)
model.eval()

# Remove last layer for feature extraction
feature_extractor = torch.nn.Sequential(*list(model.children())[:-1])

# Image transform for ResNet
transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # ImageNet mean
                         std=[0.229, 0.224, 0.225])   # ImageNet std
])

# --- Load video and extract keyframes ---
video_path = "sample.mp4"  # Replace with your video file
cap = cv2.VideoCapture(video_path)

interval = 60  # extract every 60th frame
frame_index = 0
keyframes = []
cnn_features = []
predicted_labels = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_index % interval == 0:
        # Preprocess the frame
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img_tensor = transform(rgb).unsqueeze(0)

        with torch.no_grad():
            # Get predicted class
            output = model(img_tensor)
            _, predicted = torch.max(output, 1)
            class_index = predicted.item()
            predicted_labels.append(labels[class_index])

            # Get CNN embedding (512-d)
            features = feature_extractor(img_tensor).squeeze().numpy()
            cnn_features.append(features)

            keyframes.append(frame)

    frame_index += 1

cap.release()
print(f"\nExtracted {len(keyframes)} keyframes.\n")

# --- Print predicted class for each keyframe ---
for i, label in enumerate(predicted_labels):
    print(f"Keyframe {i}: {label}")

# --- Cluster using average-linkage ---
linked = linkage(cnn_features, method='average')

# --- Show dendrogram ---
plt.figure(figsize=(10, 4))
dendrogram(linked, labels=[f"{i}: {predicted_labels[i]}" for i in range(len(keyframes))])
plt.title("Keyframe Clustering (CNN Embeddings + Semantic Labels)")
plt.xlabel("Keyframe")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()
