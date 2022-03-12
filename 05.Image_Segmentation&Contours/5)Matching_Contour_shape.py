import cv2
import numpy as np
# CHECK FOR  37
# Load the shape template or reference image
template = cv2.imread('C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Master OpenCV/images/4star.jpg',0)
cv2.imshow('Template', template)

# Load the target image with the shapes we're trying to match
target = cv2.imread('C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Master OpenCV/images/shapestomatch.jpg')
target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

# Threshold both images first before using cv2.findContours
ret1, thresh1 = cv2.threshold(template, 127, 255, 0)
ret2, thresh2 = cv2.threshold(target_gray, 127, 255, 0)

# Find contours in template
_, contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# We need to sort the contours by area so that we can remove the largest
# contour which is the image outline
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
#print(sorted_contours)
# We extract the second largest contour which will be our template contour
template_contour = contours[1]

# Extract contours from second target image
_, contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # Iterate through each contour in the target image and
    # use cv2.matchShapes to compare contour shapes
    match = cv2.matchShapes(template_contour, c, 3, 0.0)
    print(match)
    # If the match value is less than 0.15 we
    if match < 0.15:
        closest_contour = c
    else:
        closest_contour = []

cv2.drawContours(target, [closest_contour], -1, (0, 255, 0), 3)
cv2.imshow('Output', target)
cv2.waitKey()
cv2.destroyAllWindows()