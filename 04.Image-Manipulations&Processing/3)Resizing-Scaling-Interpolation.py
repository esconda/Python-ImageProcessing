import cv2
import numpy as np
import os

#CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 21
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")


    image_scaled = cv2.resize(img,None, fx=0.75, fy=0.75)
    cv2.imshow('Scaling- Lınear Interpolation',image_scaled)
    cv2.waitKey()

    #Double Size
    cubic_scaled = cv2.resize(img,None, fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Scaling- cubic Interpolation', cubic_scaled)
    cv2.waitKey()

    area_scaled = cv2.resize(img, (900,400), interpolation=cv2.INTER_AREA)
    cv2.imshow('Scaling-skewed size', area_scaled)
    cv2.waitKey()

    #-------ANOTHER WAY OF RESIZING WITH IMAGE PYRAMIDS
    #uSEFUL WHEN SCALİNG İMAGES İN OBJECT DETECTİON
    smaller = cv2.pyrDown(img)
    larger = cv2.pyrUp(smaller)

    cv2.imshow('Pyramid-smaller', smaller)
    cv2.imshow('Pyramid-larger', larger)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()