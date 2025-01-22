import cv2
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time into a string suitable for filenames
filename = now.strftime("file_%Y-%m-%d_%H-%M-%S.jpg")

print("Generated filename:", filename)

# Initialize the camera (0 is typically the default webcam; use 1 or higher if you have multiple cameras)
camera_index = 0  # Change this if needed
cap = cv2.VideoCapture(camera_index)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Set camera resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)



# Capture a frame
ret, frame = cap.read()

if ret:
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    # Save the captured image to a file
    #filename = "captured_image.jpg"
    cv2.imwrite(filename, rotated_frame)
    print(f"Image saved as {filename}")
else:
    print("Error: Could not capture an image.")

# Release the camera
cap.release()