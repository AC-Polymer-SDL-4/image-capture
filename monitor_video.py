import cv2

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

print("Press 'q' to quit the video feed.")

# Loop to continuously get frames and display them
while True:
    # Capture a single frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Display the frame in a window
    cv2.imshow("Real-Time Video Feed", rotated_frame)

    # Check for the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()