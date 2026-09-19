# Face Detector

A simple **face detection application built with Python and OpenCV**. The project uses OpenCV's Haar Cascade classifier to detect human faces in an image and draws bounding rectangles around the detected faces.

## Features

* Detects multiple faces in an image
* Uses OpenCV's Haar Cascade face classifier
* Converts the image to grayscale for detection
* Draws rectangles around detected faces
* Displays the total number of detected faces
* Handles missing or invalid image files
* Works with group photos

## Technologies Used

* **Python 3**
* **OpenCV 4.13.0**
* Haar Cascade Classifier

## Installation

Install the required OpenCV package:

```bash
pip install opencv-python==4.13.0.92
```

NumPy is installed automatically as an OpenCV dependency.

## Project Structure

```text
face-detector/
│
├── face_detector.py
├── input.jpg
├── image.png
└── README.md
```

* `face_detector.py` - Main face detection program
* `input.jpg` - Test image used for face detection
* `image.png` - Additional test image
* `README.md` - Project documentation

## How It Works

The program follows these steps:

```text
Input Image
     ↓
Load Haar Cascade Classifier
     ↓
Convert Image to Grayscale
     ↓
Detect Faces
     ↓
Draw Bounding Rectangles
     ↓
Display Detected Faces
```

The Haar Cascade classifier is loaded using OpenCV's built-in cascade data:

```python
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
```

Faces are detected using:

```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)
```

## Running the Project

Make sure `input.jpg` is present in the same folder as `face_detector.py`.

Run:

```bash
python face_detector.py
```

The program will open the image and draw a rectangle around each detected face.

Press any key while the image window is active to close it.

## Example Output

The program also displays the number of detected faces in the terminal:

```text
Faces detected: 4
Press any key to close the window.
```

The detected faces are highlighted with rectangular bounding boxes in the output image.

## Testing

The detector was tested using a **group photograph containing multiple people** to verify that the program can detect more than one face in a single image.

## Error Handling

The program checks whether the input image exists before processing it:

```text
Error: input.jpg not found!
```

It also checks whether OpenCV was able to load the image successfully.

## Learning Objectives

This project demonstrates:

* Basic computer vision concepts
* Image processing with OpenCV
* Haar Cascade face detection
* Grayscale image conversion
* Object detection
* Drawing bounding boxes
* Working with image files in Python

## Author

**Kaivalya**