# Pose Estimation using MediaPipe

This repository contains a project that uses the MediaPipe library for pose estimation on both images and videos. It can detect and track human body landmarks in real-time or from static images and videos.

## Project Structure

The project is organized as follows:

- **res/images**: This directory contains static images for pose estimation.
  - Add your image files here.

- **res/videos**: This directory contains video files for real-time pose estimation.
  - Add your video files here.

- `media.py`: This Python script performs pose estimation on static images.
  
- `video.py`: This Python script performs real-time pose estimation on videos.

## How to Use

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/pose-estimation-mediapipe.git
2. Run media.py to perform pose estimation on static images:
  ```bash
  python media.py
