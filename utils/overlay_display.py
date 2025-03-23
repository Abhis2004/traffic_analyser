import cv2

def draw_overlays(frame, tracked_vehicles, speeds, plates, weather):
    """
    Draws bounding boxes, speed, license plates, and weather information on the frame.

    Parameters:
    - frame: The current video frame.
    - tracked_vehicles: List of tuples [(x1, y1, x2, y2, vehicle_id), ...].
    - speeds: Dictionary {vehicle_id: speed}.
    - plates: Dictionary {vehicle_id: plate_number}.
    - weather: String indicating the detected weather condition.

    Returns:
    - Modified frame with overlays drawn.
    """
    for vehicle in tracked_vehicles:
        if len(vehicle) != 5:
            continue  # Skip if the tuple is not complete

        x1, y1, x2, y2, vehicle_id = vehicle  # Unpack the tuple

        # Draw bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Display speed
        speed_text = f"Speed: {speeds.get(vehicle_id, 'N/A')} km/h"
        cv2.putText(frame, speed_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                    1.0, (0, 255, 255), 3)

        # Display license plate
        plate_number = plates.get(vehicle_id, "N/A")
        cv2.putText(frame, f"Plate: {plate_number}", (x1, y2 + 30), cv2.FONT_HERSHEY_SIMPLEX, 
                    1.0, (255, 0, 0), 3)

    # Display weather information in the top-left corner
    cv2.putText(frame, f"Weather: {weather}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 
                1.2, (255, 255, 255), 3)

    return frame
