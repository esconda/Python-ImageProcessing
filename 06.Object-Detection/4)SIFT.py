import cv2
import numpy as np
#CHECK FOR  46
image = cv2.imread("D:/Tutorials/Python-Tutorials/Python_Opencv-Tutorials-Examples/Master_OpenCV/images/input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Create SIFT Feature Detector object
sift = cv2.xfeatures2d.SIFT_create()

#Detect key points
keypoints = sift.detect(gray, None)
print("Number of keypoints Detected: ", len(keypoints))

# Draw rich key points on input image
image = cv2.drawKeypoints(image, keypoints,None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


# SIFT, SURF, FAST, BRIEF & ORB

cv2.imshow('Feature Method - SIFT', image)
cv2.waitKey(0)
cv2.destroyAllWindows()