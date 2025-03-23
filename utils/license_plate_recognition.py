# import easyocr

# reader = easyocr.Reader(['en'])  # Load the EasyOCR model

# def recognize_license_plate(frame, vehicles):
#     plates = {}
#     for i, (x1, y1, x2, y2) in enumerate(vehicles):
#         plate_region = frame[y1:y2, x1:x2]  # Crop the plate area
#         result = reader.readtext(plate_region)  # Perform OCR
#         if result:
#             plates[i] = result[0][-2]  # Extract recognized text
#     return plates


import easyocr

reader = easyocr.Reader(['en'])  # Load the EasyOCR model

def recognize_license_plate(frame, vehicles):
    plates = {}
    for x1, y1, x2, y2, vehicle_id in vehicles:
        plate_region = frame[y1:y2, x1:x2]  # Crop the plate area
        result = reader.readtext(plate_region)  # Perform OCR
        if result:
            plates[vehicle_id] = result[0][-2]  # Extract recognized text
    return plates