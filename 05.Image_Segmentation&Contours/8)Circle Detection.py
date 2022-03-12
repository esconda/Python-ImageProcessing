import cv2
import numpy as np

# CHECK FOR  39

image = cv2.imread('C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Master OpenCV/images/bottlecaps.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(gray, 5)
cv2.imshow("blured image", blur)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.5, 10,param1=100,
              param2=50,
              minRadius=40,
              maxRadius=50)
# circles = cv2.HoughCircles(gray, cv.CV_HOUGH_GRADIENT, 1, 10)

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(image, (i[0], i[1]), i[2], (255, 0, 0), 2)

    # draw the center of the circle
    cv2.circle(image, (i[0], i[1]), 2, (0, 255, 0), 5)

cv2.imshow('detected circles', image)
cv2.waitKey(0)
cv2.destroyAllWindows()