# OpenCV 2.4.13 only
import numpy as np
import cv2

# Intialize Webcam
cap = cv2.VideoCapture(0)

# Initlaize background subtractor
foreground_background = cv2.createBackgroundSubtractorMOG2()

while True:

    ret, frame = cap.read()

    # Apply background subtractor to get our foreground mask
    foreground_mask = foreground_background.apply(frame)
    erosion = cv2.erode(foreground_mask, None, iterations=1)

    cv2.imshow('Output', erosion)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()