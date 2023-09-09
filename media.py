import cv2
import mediapipe as mp

# Load the image
image_path = 'res/images/virat.jpg'  # Replace with the actual image path
image = cv2.imread(image_path)

if image is None:
    print(f"Failed to load image from path: {image_path}")
    exit()

# Set up Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Resize the image for better visualization
resized_image = cv2.resize(image, (800, 600))

# Convert the resized image to RGB
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)

# Detect the pose in the resized image
with mp_pose.Pose(static_image_mode=True) as pose:
    results = pose.process(resized_image_rgb)

    # Draw the pose landmarks on the resized image
    annotated_image = resized_image.copy()
    mp_drawing.draw_landmarks(annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the annotated image
    cv2.imshow("Annotated Image", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
