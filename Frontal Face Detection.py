import cv2

# Load the face cascade classifier
face_cascade = cv2.CascadeClassifier('C:/Users/ASUS/Downloads/XML files/haarcascade_frontalface_default.xml')


# Initialize the webcam capture
cap = cv2.VideoCapture(0)

# Loop through the frames from the webcam stream
while True:
    # Read a frame from the webcam stream
    ret, frame = cap.read()
    
    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Loop through the detected faces and draw a rectangle and a line around each face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Draw a line from one corner of the rectangle to a circle
        center_x, center_y = x + w // 2, y + h // 2
        radius = max(w, h) // 2
        cv2.line(frame, (x, y), (center_x, center_y), (255, 0, 0), 2)
        cv2.circle(frame, (center_x, center_y), radius, (255, 0, 0), 2)
        
        # Display a text box with the assumed age of the person
        age = "51"
        cv2.putText(frame, f"Assumed Age: {age}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Display the processed frame
    cv2.imshow('Face Detection', frame)
    
    # Wait for a key press and check if it is the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
