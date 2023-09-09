import cv2
import mediapipe as mp
import time

# Import necessary libraries

# Initialize MediaPipe drawing utilities
mpDraw = mp.solutions.drawing_utils
# Initialize MediaPipe pose estimation
mpPose = mp.solutions.pose
# Create an instance of the Pose class
pose = mpPose.Pose()

# Open the video file
cap = cv2.VideoCapture('res/videos/yoga.mp4')

# Initialize previous frame time
pTime = 0

# Process each frame of the video
while True:
    # Read the next frame from the video
    success, img = cap.read()

    # Resize the frame for better visualization
    resized_frame = cv2.resize(img, (800, 600))

    # Convert the frame from BGR to RGB
    imgRGB = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)

    # Process the RGB image with the pose estimation model
    results = pose.process(resized_frame)

    # Check if any pose landmarks were detected
    if results.pose_landmarks:
        # Draw the pose landmarks on the image
        mpDraw.draw_landmarks(resized_frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

        # Iterate over each pose landmark
        for id, lm in enumerate(results.pose_landmarks.landmark):
            # Get the frame dimensions
            h, w, c = resized_frame.shape

            # Print the landmark ID and coordinates
            print(id, lm)

            # Calculate the pixel coordinates of the landmark
            cx, cy = int(lm.x * w), int(lm.y * h)

            # Draw a circle at the landmark position
            cv2.circle(resized_frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    # Calculate the frame rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display the frame rate on the image
    cv2.putText(resized_frame, str(int(fps)), (10, 30), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Show the image with the pose landmarks
    cv2.imshow("Image", resized_frame)

    # Check for the "q" key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
cap.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
