# ==========================================
# Face Detection Project
# Developed as AI/ML Project
# ==========================================

import cv2
from datetime import datetime


# ==========================================
# Load Pre-trained Face Detector
# ==========================================

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# ==========================================
# Open Webcam
# ==========================================

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()


# ==========================================
# Face Detection Loop
# ==========================================

while True:

    success, frame = camera.read()

    if not success:
        print("Error: Could not read webcam frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Count faces
    face_count = len(faces)

    # Display total number of faces
    cv2.putText(
        frame,
        f"Faces Detected: {face_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Draw boxes and labels
    for number, (x, y, w, h) in enumerate(faces, start=1):

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            f"Face {number}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 0, 0),
            2
        )

    # Show camera window
    cv2.imshow("Face Detection", frame)

    # Read keyboard input
    key = cv2.waitKey(1) & 0xFF

    # ==========================================
    # Press S to Save Photo with Timestamp
    # ==========================================

    if key == ord("s"):

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        filename = f"detected_faces_{timestamp}.jpg"

        cv2.imwrite(filename, frame)

        print(f"Photo saved as {filename}")

    # ==========================================
    # Press Q to Quit
    # ==========================================

    if key == ord("q"):
        break


# ==========================================
# Release Camera
# ==========================================

camera.release()
cv2.destroyAllWindows()

print("Face Detection program closed successfully.")