import cv2
import torch
from ultralytics import YOLO
from utils.vehicle_tracking import track_vehicles
from utils.speed_estimation import estimate_speed
from utils.license_plate_recognition import recognize_license_plate
from utils.weather_detection import detect_weather
from utils.overlay_display import draw_overlays

# Video settings
VIDEO_PATH = "data/test_video2.mp4"
FPS = 30
PIXELS_PER_METER = 10

# Load YOLO model
yolo_model = YOLO("models/yolov8n.pt")
cap = cv2.VideoCapture(VIDEO_PATH)

previous_positions = {}

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Ensure frame retains original resolution
        frame_height, frame_width = frame.shape[:2]
        
        # Detect Weather
        weather = detect_weather(frame)

        # Vehicle Detection using YOLO
        results = yolo_model(frame)
        vehicles = []

        for result in results:
            for box in result.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box[:4])  # Extract bounding box
                vehicles.append((x1, y1, x2, y2))

        # Track Vehicles
        tracked_vehicles = track_vehicles(vehicles)

        # Estimate Speed
        speeds = estimate_speed(tracked_vehicles, previous_positions)

        # License Plate Recognition
        plates = recognize_license_plate(frame, tracked_vehicles)

        # Draw Overlays
        frame = draw_overlays(frame, tracked_vehicles, speeds, plates, weather)

        # Ensure the window displays correctly without zooming
        cv2.namedWindow("Traffic Analysis", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Traffic Analysis", frame_width, frame_height)
        cv2.imshow("Traffic Analysis", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

process_video(VIDEO_PATH)