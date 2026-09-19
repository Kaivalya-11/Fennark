import cv2
import os

# Load the Haar Cascade face classifier
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

face_cascade = cv2.CascadeClassifier(cascade_path)

# Get the folder where this Python file is located
project_folder = os.path.dirname(os.path.abspath(__file__))

# Image path
image_path = os.path.join(project_folder, "input.jpg")

# Check if image exists
if not os.path.exists(image_path):
    print("Error: input.jpg not found!")
    print("Place input.jpg in the same folder as face_detector.py")
    exit()

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

print(f"Faces detected: {len(faces)}")

# Display result
cv2.imshow("Face Detector", image)

print("Press any key to close the window.")
cv2.waitKey(0)
cv2.destroyAllWindows()