# Real-Time Emotion Recognition

A lightweight Python script that captures live video from your webcam, analyzes facial expressions using DeepFace’s pre-trained emotion model, and displays the detected “dominant emotion” on each frame in real time.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Demo](#demo)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Usage](#usage)
7. [How It Works](#how-it-works)
8. [Troubleshooting & Tips](#troubleshooting--tips)
9. [License](#license)

---

## Project Overview

This repository contains a Python script (`emotion_recognition.py`) that:

* Grabs live video frames from your webcam using OpenCV.
* Sends each frame to DeepFace for emotion analysis (happy, sad, surprised, angry, etc.).
* Overlays the detected “dominant emotion” onto the video feed in real time.
* Continues running until you press **q** to quit.

This demo is intended to showcase a simple end-to-end pipeline for real-time computer vision + emotion recognition using readily available open-source tools.

---

## Features

* **Live Webcam Capture**: Streams frames from your default webcam using OpenCV.
* **DeepFace Emotion Analysis**: Utilizes DeepFace’s pre-trained emotion detector to identify the dominant emotion per frame.
* **Real-Time Overlay**: Draws the detected emotion text on each frame via OpenCV’s `putText`.
* **Lightweight & Self-Contained**: Only one Python script—minimal dependencies.
* **Immediate Feedback**: Run the script and see “Emotion: \[label]” displayed in the top-left corner of the live video window. Press **q** to exit gracefully.

---

## Demo

![Screenshot of Emotion Recognition Demo](docs/screenshot.png)

> *Note: Depending on your webcam’s resolution and lighting conditions, the text placement and clarity may vary.*

---

## Requirements

* **Python 3.7+**
* **OpenCV** (`opencv-python`)
* **DeepFace** (`deepface`)
* A working webcam

---

## Installation

1. **Clone this Repository**

   ```bash
   git clone https://github.com/your-username/real-time-emotion-recognition.git
   cd real-time-emotion-recognition
   ```

2. **Create a Virtual Environment (Recommended)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on Linux/Mac
   venv\Scripts\activate      # on Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install --upgrade pip
   pip install opencv-python deepface
   ```

   * If you run into installation errors, ensure you’re using a compatible Python version (≥ 3.7) and that `pip` is up to date.

---

## Usage

1. **Run the Script**
   Open a terminal (with the virtual environment activated, if applicable) and execute:

   ```bash
   python emotion_recognition.py
   ```

2. **Allow Camera Access** (if prompted).

3. **Observe the Video Window**

   * A window titled **“Emotion Recognition”** will appear, streaming live feed from your webcam.
   * You should see text like **“Emotion: happy”** or **“Emotion: neutral”** updating in real time.

4. **Quit**

   * Press **q** on your keyboard to stop the script and close the window.

---

## How It Works

1. **Capture Frame**

   ```python
   cap = cv2.VideoCapture(0)
   ret, frame = cap.read()
   ```

   * Initializes video capture from the default webcam (`0`).
   * Reads a single frame (`frame`) each iteration.

2. **Emotion Analysis**

   ```python
   results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
   emotion = results[0]['dominant_emotion']
   ```

   * Uses `DeepFace.analyze(...)` to run inference on the captured frame.
   * `actions=['emotion']` specifies we only want emotion predictions.
   * `enforce_detection=False` tells DeepFace to skip raising an error if no face is detected.

3. **Overlay Text**

   ```python
   cv2.putText(
       frame,
       f'Emotion: {emotion}',
       (50, 50),
       cv2.FONT_HERSHEY_SIMPLEX,
       1,
       (255, 0, 0),
       2
   )
   ```

   * Draws the string **“Emotion: {emotion}”** at coordinates (50, 50) in the frame.
   * Uses a blue font `(BGR = 255, 0, 0)` with thickness 2.

4. **Display Frame**

   ```python
   cv2.imshow("Emotion Recognition", frame)
   if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   ```

   * Shows the annotated frame in a window titled **“Emotion Recognition”**.
   * Every loop iteration calls `cv2.waitKey(1)`, and if you press **q** it breaks out of the loop.

5. **Cleanup**

   ```python
   cap.release()
   cv2.destroyAllWindows()
   ```

   * Releases the webcam resource and closes all OpenCV windows upon exit.

---

## Troubleshooting & Tips

* **Webcam Not Detected**

  * Ensure no other application is using the camera.
  * Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` (or another index) if your default device isn’t at index 0.

* **Laggy Performance**

  * Emotion inference can be compute-intensive. Consider using a machine with a dedicated GPU or reducing the webcam resolution:

    ```python
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    ```

* **DeepFace Errors**

  * If DeepFace reports missing backend libraries, install TensorFlow or PyTorch explicitly:

    ```bash
    pip install tensorflow   # or
    pip install torch torchvision
    ```

* **enforce\_detection=False**

  * With `enforce_detection=False`, DeepFace skips errors when no face is found, returning the last valid output instead. If strict face detection is required, set `enforce_detection=True`, but be prepared for possible runtime errors when no face is visible.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

> **Happy coding!** If you find this project useful or have ideas for improvements, please ⭐ star this repo, open an issue, or submit a pull request.
