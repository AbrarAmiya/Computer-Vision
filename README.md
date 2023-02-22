# Open-CV
OpenCV is the huge open-source library for computer vision, ML, and image processing and now it plays a major role in real-time operation which is very important in today's systems. By using it, one can process images and videos to identify objects, faces, or even the handwriting of a human.
This is a Python code using OpenCV library to detect faces in real-time video stream from a webcam and draw a rectangle, a line, and a text box around each detected face.

The code starts by importing the OpenCV library and loading a pre-trained classifier for face detection. Then, it initializes the webcam capture and enters into a loop to continuously read frames from the video stream.

In each iteration of the loop, the code converts the color image to grayscale to perform face detection. It applies the face detection algorithm using the detectMultiScale method of the face_cascade object and stores the detected
