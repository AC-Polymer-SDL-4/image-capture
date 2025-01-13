import cv2
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time into a string suitable for filenames
filename = now.strftime("file_%Y-%m-%d_%H-%M-%S.jpg")

print("Generated filename:", filename)

# Initialize the camera (0 is typically the default webcam; use 1 or higher if you have multiple cameras)
camera_index = 1  # Change this if needed
cap = cv2.VideoCapture(camera_index)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Set camera resolution (optional)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

common_resolutions = [
    (1920, 1080), (1280, 720), (640, 480),
    (480, 480), (320, 240)
]

for width, height in common_resolutions:
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    actual_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    actual_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    if actual_width == width and actual_height == height:
        print(f"Supported resolution: {width}x{height}")
    else:
        print(f"Failed to set resolution: {width}x{height}")


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