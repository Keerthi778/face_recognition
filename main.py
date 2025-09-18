import cv2
import numpy as np

def resize_frame(frame, max_width=1280, max_height=720):
    """Resize frame to fit within specified dimensions while maintaining aspect ratio"""
    height, width = frame.shape[:2]
    scale = min(max_width/width, max_height/height)
    if scale < 1:
        return cv2.resize(frame, (int(width*scale), int(height*scale)))
    return frame

# Load pre-trained face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the default camera (webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    cv2.namedWindow("Detected Faces", cv2.WINDOW_NORMAL)
    frame_count = 0
    max_frames = 100  # Change this value to the number of frames you want to process
    while True:
        ret, frame = cap.read()
        if not ret or frame_count >= max_frames:
            print("Video stopped automatically.")
            break
        frame = resize_frame(frame, max_width=1280, max_height=720)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("Detected Faces", frame)
        frame_count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Video stopped by user.")
            break
    cap.release()
    cv2.destroyAllWindows()
    print("Face detection complete.")