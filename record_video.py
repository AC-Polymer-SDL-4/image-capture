import cv2
from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time into a string suitable for filenames
output_filename = now.strftime("file_%Y-%m-%d_%H-%M-%S.avi")

# Initialize the camera (0 is typically the default webcam; change it if needed)
camera_index = 0
cap = cv2.VideoCapture(camera_index)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Set camera resolution (optional)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Variables for recording
is_recording = False
video_writer = None
#output_filename = "output.avi"
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30

print("Press 'r' to start recording, 's' to stop recording, and 'q' to quit.")

# Loop to continuously get frames and display them
while True:
    # Capture a single frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Rotate the frame (if needed)
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # If recording, write the frame to the video file
    if is_recording and video_writer:
        video_writer.write(rotated_frame)

    # Display the frame in a window
    cv2.imshow("Real-Time Video Feed", rotated_frame)

    # Check for key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Quit the program
        break
    elif key == ord('r') and not is_recording:  # Start recording
        print("Recording started.")
        is_recording = True
        video_writer = cv2.VideoWriter(
            output_filename,
            cv2.VideoWriter_fourcc(*'XVID'),
            fps,
            (frame_height, frame_width)
        )
    elif key == ord('r') and is_recording:  # Stop recording
        print("Recording stopped.")
        is_recording = False
        if video_writer:
            video_writer.release()
            video_writer = None

# Release the camera and close all OpenCV windows
cap.release()
if video_writer:
    video_writer.release()
cv2.destroyAllWindows()