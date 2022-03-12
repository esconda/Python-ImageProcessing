import cv2
import numpy as np
import os

#CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 23
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")
    height,width = img.shape[:2]

    Matrix = np.ones(img.shape,np.uint8)*75

    #adding brightness
    brigthing_image = cv2.add(img,Matrix)
    cv2.imshow('Bright-Image', brigthing_image)
    cv2.waitKey()

    #decrease brightness
    Dark_image = cv2.subtract(img, Matrix)
    cv2.imshow('Dark-Image', Dark_image)
    cv2.waitKey()


    cv2.imshow('Original-Image', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()