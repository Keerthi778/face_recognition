

# Face Detection with OpenCV

This project demonstrates real-time **face detection** using Python and OpenCV. It uses a pre-trained Haar Cascade classifier to detect faces from a live webcam feed, draws bounding boxes around detected faces, and displays the result in a resizable window.

---

## 📌 Features

* Captures video from the default webcam.
* Detects faces using OpenCV’s Haar Cascade classifier.
* Draws blue rectangles around detected faces.
* Resizes frames to fit within `1280x720` while maintaining aspect ratio.
* Stops automatically after a fixed number of frames (default: 100).
* Can be stopped manually by pressing **`q`**.

---

## 🚀 Requirements

Make sure you have Python installed (>=3.7 recommended). Install dependencies with:

```bash
pip install opencv-python numpy
```

---

## ▶️ Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/face-detection-opencv.git
   cd face-detection-opencv
   ```
2. Run the script:

   ```bash
   python face_detection.py
   ```
3. A window will open showing the webcam feed with detected faces.

* Press **`q`** to exit manually.
* Otherwise, the script stops automatically after 100 frames.

---

## ⚙️ Configuration

You can tweak a few parameters inside the script:

* **`max_frames`** → Maximum frames to process (default: 100).
* **`max_width` / `max_height`** → Resize limits for display window (default: `1280x720`).
* **Haar Cascade parameters** (`scaleFactor`, `minNeighbors`) → Adjust face detection sensitivity.

---

## 📂 File Structure

```
.
├── face_detection.py   # Main script
└── README.md           # Project documentation
```

---

## 📷 Example Output

Detected faces are highlighted with rectangles in real-time:

```
[ Webcam feed with blue rectangles around faces ]
```

---

## 📖 References

* [OpenCV Documentation](https://docs.opencv.org/)
* [Haar Cascade Classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)

---

