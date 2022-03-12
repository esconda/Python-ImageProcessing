import cv2
import numpy as np
import os

#CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 24,25
def main():

    #Making Squre
    square = np.zeros((300,300),np.uint8)
    print(square.shape)
    cv2.rectangle(square,(50,50), (250,250), 100, -2)
    cv2.imshow('Square', square)
    cv2.waitKey(0)

    ellipse = np.zeros((300, 300), np.uint8)
    cv2.ellipse(ellipse, (150, 150), (150, 150),30,0,180,255, -1)
    cv2.imshow('Ellipse', ellipse)
    cv2.waitKey(0)

    #Shows only where they intersect
    And_op = cv2.bitwise_and(square,ellipse)
    cv2.imshow("AND",And_op)
    cv2.waitKey(0)

    #Shows where either square or ellipse is
    Or_op = cv2.bitwise_or(square, ellipse)
    cv2.imshow("OR", Or_op)
    cv2.waitKey(0)

    # Shows everything that isnt part of the square
    Not_op = cv2.bitwise_not(square)
    cv2.imshow("NOT-Square", Not_op)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
if __name__ == '__main__':
    main()