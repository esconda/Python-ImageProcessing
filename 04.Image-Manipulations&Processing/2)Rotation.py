import cv2
import numpy as np
import os


def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")

    #Store height and width of the image
    height, width = img.shape[:2]

    quarter_height,quarter_width = height/4, width/4

    #Divide by two to rotate the image around its centre
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2),30,1)

    #forward rotation matrix
    rotated_image = cv2.warpAffine(img,rotation_matrix,(width,height))

    #other option to rotate
    rotated_image_2 = cv2.transpose(img)

    cv2.imshow("My another image", img)
    cv2.imshow('Rotated Image',rotated_image)
    cv2.imshow('Rotated Image 2', rotated_image_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()