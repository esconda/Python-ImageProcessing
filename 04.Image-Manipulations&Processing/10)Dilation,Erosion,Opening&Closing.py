import cv2
import numpy as np
import os


# CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 28
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/4.jpg", 0)
    cv2.imshow("Original", img)

    kernel = np.ones((5,5),np.uint8)

    #Erosion,extend black areas
    erosion = cv2.erode(img,kernel,iterations=1)
    cv2.imshow("Erosion", erosion)

    #Dilation,extend white areas
    dilation = cv2.dilate(img,kernel,iterations=1)
    cv2.imshow("Dilation", dilation)

    #Opening
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening", opening)

    #Closing
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing", closing)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()