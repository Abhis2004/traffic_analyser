import cv2
import numpy as np

def detect_weather(frame):
    """
    Detects weather conditions (Sunny, Cloudy, Foggy, Rainy, Night) based on brightness & contrast.
    :param frame: Input frame
    :return: Weather condition as a string
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = gray.mean()
    contrast = np.std(gray)

    if brightness < 50:
        return "Night"
    elif contrast < 20:
        return "Foggy"
    elif brightness < 120:
        return "Cloudy"
    elif brightness > 180:
        return "Sunny"
    else:
        return "Rainy"
