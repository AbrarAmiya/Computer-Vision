import cv2

# initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # read frame from webcam
    ret, frame = cap.read()
    
    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # apply threshold to filter out black pixels
    ret, thresh = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)
    
    # find contours in thresholded image
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # loop over contours and find the one with the largest area
    max_area = 0
    max_contour = None
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            max_contour = contour
    
    # draw contour on original frame
    if max_contour is not None:
        cv2.drawContours(frame, [max_contour], 0, (0, 255, 0), 2)
    
    # show original frame
    cv2.imshow('frame', frame)
    
    # exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
