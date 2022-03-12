import cv2
import numpy as np
import os

#CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 27
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")
    cv2.imshow("Original", img)

    #Create our sharpening kernel, we don't normalize since the
    #the values in the matrix sum to 1
    kernel_sharpening = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])


    sharpened = cv2.filter2D(img,-1,kernel_sharpening)

    cv2.imshow("Image Sharpening", sharpened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()