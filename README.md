# Traffic Analyser

Traffic Analyser is a Python-based project designed to process video footage and analyze traffic-related data. It uses advanced computer vision techniques to detect vehicles, track their movements, estimate their speeds, recognize license plates, and even detect weather conditions. The processed video is displayed with overlays showing all the extracted information.

---

## Table of Contents
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
6. [Dependencies](#dependencies)
7. [Contributing](#contributing)

---

## Features

- **Vehicle Detection**: Detects vehicles in video frames using the YOLO (You Only Look Once) object detection model.
- **Vehicle Tracking**: Tracks vehicles across frames and assigns unique IDs to each vehicle.
- **Speed Estimation**: Calculates the speed of vehicles based on their movement across frames.
- **License Plate Recognition**: Recognizes license plates using Optical Character Recognition (OCR).
- **Weather Detection**: Analyzes video frames to determine weather conditions (e.g., sunny, rainy).
- **Overlay Display**: Displays bounding boxes, speeds, license plate numbers, and weather information on the video.
- **Real-Time Processing**: Processes video frame by frame and displays the output in real-time.

---

## Project Structure

traffic_analyser/ │ ├── main.py # Main script to run the traffic analysis ├── data/ # Folder containing video files │ ├── test_video.mp4 │ ├── test_video1.mp4 │ └── test_video2.mp4 ├── models/ # Folder containing YOLO model files │ ├── yolov8_plate.pt │ ├── yolov8_vehicle.pt │ └── yolov8n.pt ├── outputs/ # Folder for saving processed outputs (if implemented) ├── sort/ # SORT (Simple Online and Realtime Tracking) implementation │ ├── sort.py │ ├── LICENSE │ └── README.md ├── utils/ # Utility scripts for various functionalities │ ├── utils/license_plate_recognition.py │ ├── overlay_display.py │ ├── speed_estimation.py │ ├── vehicle_tracking.py │ └── weather_detection.py └── requirements.txt # List of dependencies

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Abhis2004/traffic_analyser.git
   cd traffic_analyser

2. Install the required dependencies:

3. Download the YOLO model weights:
    Place the YOLO model files (yolov8n.pt, yolov8_vehicle.pt, yolov8_plate.pt) in the models/ directory.
4. Install additional tools:
    Install EasyOCR for license plate recognition:
    ```bash
    pip install easyocr

## Usage

1. Place your video files in the data/ directory.
2. Open the main.py file and set the VIDEO_PATH variable to the path of your video file (e.g., data/test_video2.mp4).
3. Run the script:
    python main.py
4. The processed video will be displayed in a window titled "Traffic Analysis." Press q to exit the video.

## How It Works

1. Video Input:
    The script reads video frames from the specified file using OpenCV.

2. Vehicle Detection:
    The YOLO model detects vehicles in each frame and outputs bounding boxes.

3. Vehicle Tracking:
    Detected vehicles are tracked across frames using a tracking algorithm, assigning unique IDs to each vehicle.

4. Speed Estimation:
    The speed of each vehicle is calculated based on its movement across frames and the frame rate (FPS).

5. License Plate Recognition:
    The license plate region is cropped from the frame, and OCR is applied to extract the text.

6. Weather Detection:
    The frame is analyzed to determine weather conditions using a custom weather detection function.

7. Overlay Display:
    Bounding boxes, speeds, license plate numbers, and weather information are drawn on the video frames.
8. Output Display:
    The processed video is displayed in real-time.

## Dependencies

The project uses the following libraries:

> OpenCV - For video processing and display.

> Ultralytics YOLO - For vehicle detection.

> EasyOCR - For license plate recognition.

> NumPy - For numerical operations.

> PyTorch - For running the YOLO model.

> Install all dependencies using:
    ```bash
    pip install -r requirements.txt
    ```
## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to open an issue or submit a pull request.