import cv2
import numpy as np
import os


# CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 30
#SOBEL , LAPLACIAN, CANNY
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/4.jpg", 0)
    cv2.imshow("Original", img)

    height,width = img.shape

    #Extract Sobel Edges
    sobel_x = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)

    cv2.imshow('Sobel_x',sobel_x)
    cv2.imshow('Sobel_y', sobel_y)

    #Birleşim
    sobel_Or = cv2.bitwise_or(sobel_x,sobel_y)
    cv2.imshow('Sobel_or', sobel_Or)

    #Laplacian
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    cv2.imshow('Laplacian',laplacian)

    #Canny
    canny = cv2.Canny(img,20,170)
    cv2.imshow('Canny',canny)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()