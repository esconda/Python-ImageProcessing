import cv2
import numpy as np
import os

#CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 28
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg",1)
    cv2.imshow("Original",img)

    #THRESHOLDING METHODS
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    cv2.imshow("1)Threshold Binary",thresh1)

    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("2)Threshold Inverse-Binary",thresh2)

    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    cv2.imshow("3)Threshold Binary-Truncated",thresh3)

    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    cv2.imshow("4)Threshold Tozero", thresh4)

    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow("3)Threshold Tozero-Inverse", thresh5)
    
    #ADAPTIVE THRESHOLDING
    #Removing noise with gaussian blur
    # img = cv2.GaussianBlur(img, (3,3), 0)
    #
    # adaptivethresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
    # cv2.imshow("Adaptive thresh", adaptivethresh)
    #
    # _,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imshow("Otsu's Thresholding",th2)
    #
    # blur = cv2.GaussianBlur(img,(5,5),0)
    # _,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # cv2.imshow("Gaussian Otsu's Thresholding",th3)

    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()