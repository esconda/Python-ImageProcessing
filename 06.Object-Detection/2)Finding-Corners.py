import cv2
import numpy as np
#CHECK FOR  45
# Load image then grayscale
image = cv2.imread('C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Master OpenCV/images/chess.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# The cornerHarris function requires the array datatype to be float32
gray = np.float32(gray)

harris_corners = cv2.cornerHarris(gray, 3, 3, 0.05)
cv2.imshow("Harris Corners Before Harris",harris_corners)

#We use dilation of the corner points to enlarge them\
kernel = np.ones((7,7),np.uint8)
harris_corners = cv2.dilate(harris_corners, kernel, iterations = 2)
cv2.imshow("Dilation on Harris", harris_corners)

# Threshold for an optimal value, it may vary depending on the image.
print(image[harris_corners > 0.025 * harris_corners.max() ])
image[harris_corners > 0.025 * harris_corners.max() ] = [255, 127, 127]

cv2.imshow('Harris Corners', image)
cv2.waitKey(0)
cv2.destroyAllWindows()