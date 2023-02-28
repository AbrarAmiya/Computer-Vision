import cv2

# initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # read frame from webcam
    ret, frame = cap.read()
    
    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # apply threshold to filter out black pixels
    ret, thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)
    
    # find contours in thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # loop over contours and draw them on original frame
    for contour in contours:
        cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)
    
    # show original frame
    cv2.imshow('frame', frame)
    
    # exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
