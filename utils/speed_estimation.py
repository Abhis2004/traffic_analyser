PIXELS_PER_METER = 10  # Adjust based on calibration
FPS = 30  # Frames per second

def estimate_speed(tracked_vehicles, previous_positions):
    """
    Estimates the speed of each vehicle.
    :param tracked_vehicles: List of tracked vehicles [(x1, y1, x2, y2, ID)]
    :param previous_positions: Dictionary to store previous positions
    :return: Dictionary with vehicle IDs as keys and speeds as values
    """
    speeds = {}

    for x1, y1, x2, y2, ID in tracked_vehicles:
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        if ID in previous_positions:
            prev_x, prev_y = previous_positions[ID]
            distance = ((center_x - prev_x) ** 2 + (center_y - prev_y) ** 2) ** 0.5
            speed = (distance / PIXELS_PER_METER) * FPS * 3.6  # Convert to km/h
            speeds[ID] = round(speed, 2)

        previous_positions[ID] = (center_x, center_y)

    return speeds
