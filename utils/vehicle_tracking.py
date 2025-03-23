import numpy as np
from sort.sort import Sort  # Using SORT for tracking

# Initialize the tracker
tracker = Sort()

def track_vehicles(vehicles):
    """
    Tracks vehicles across frames using SORT.
    :param vehicles: List of bounding boxes [(x1, y1, x2, y2)]
    :return: List of tracked vehicle bounding boxes with IDs [(x1, y1, x2, y2, ID)]
    """
    if len(vehicles) == 0:
        return []
    
    detections = np.array(vehicles)
    tracked_objects = tracker.update(detections)

    return [(int(x1), int(y1), int(x2), int(y2), int(ID)) for x1, y1, x2, y2, ID in tracked_objects]