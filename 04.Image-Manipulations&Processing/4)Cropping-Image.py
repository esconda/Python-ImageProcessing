import cv2
import numpy as np
import os

#CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 22
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")
    height,width = img.shape[:2]

    cropped_image = img[20:100,30:300] #cropped image

    cv2.imshow('Cropped-Image', cropped_image)
    cv2.imshow('Original-Image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()