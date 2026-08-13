# Face Detection Project

## 📌 Project Overview

This project is a real-time **Face Detection System** developed using Python and OpenCV.

The system uses a computer's webcam to detect human faces in real time. It draws a rectangle around each detected face, counts the total number of faces, labels each detected face, and allows the user to save detected-face images with a timestamp.

## ✨ Features

* 📷 Real-time webcam access
* 👤 Detects human faces
* 👥 Detects multiple faces at the same time
* 🔢 Counts detected faces
* 🏷️ Labels faces as Face 1, Face 2, etc.
* 🖼️ Draws a rectangle around each detected face
* 💾 Saves detected-face images
* ⏰ Adds a timestamp to saved images

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy
* Haar Cascade Classifier

## 📁 Project Structure

```text
FACE_DETECTION/
│
├── src/
│   └── face_detection.py
│
├── venv/
│
├── detected_faces_YYYY-MM-DD_HH-MM-SS.jpg
│
└── README.md
```

## ⚙️ Installation

### 1. Create and activate the virtual environment

```powershell
python -m venv venv
```

Activate it in PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 2. Install OpenCV

```powershell
pip install opencv-python==4.13.0.92
```

## ▶️ How to Run

Make sure the virtual environment is activated.

Run:

```powershell
python src\face_detection.py
```

The webcam will open and the system will start detecting faces.

## ⌨️ Keyboard Controls

| Key | Action                        |
| --- | ----------------------------- |
| `S` | Save the current camera frame |
| `Q` | Quit the camera               |

Saved images are automatically given a timestamped filename.

Example:

```text
detected_faces_2026-08-13_22-10-24.jpg
```

## 🧠 How It Works

The system uses OpenCV's pre-trained **Haar Cascade Classifier** to detect faces.

The basic process is:

1. Open the webcam.
2. Capture video frames.
3. Convert each frame to grayscale.
4. Detect faces using the Haar Cascade classifier.
5. Draw rectangles around detected faces.
6. Count and label the faces.
7. Display the result in real time.
8. Save an image when the user presses `S`.

## 🎯 Project Goal

The goal of this project is to demonstrate the practical use of **Computer Vision** and **Face Detection** using Python and OpenCV.

## 👩‍💻 Developer

**AI/ML Project**

Built as a practical Computer Vision project using Python and OpenCV.
