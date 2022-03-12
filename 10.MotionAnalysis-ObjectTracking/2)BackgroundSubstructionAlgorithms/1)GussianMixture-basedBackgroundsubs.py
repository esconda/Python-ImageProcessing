import numpy as np
import cv2

cap = cv2.VideoCapture('C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Master OpenCV/Images/walking.avi')

# Initlaize background subtractor
foreground_background = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:

    ret, frame = cap.read()

    # Apply background subtractor to get our foreground mask
    foreground_mask = foreground_background.apply(frame)

    cv2.imshow('Output', foreground_mask)

    #You can continue with findcontours algorithm
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()