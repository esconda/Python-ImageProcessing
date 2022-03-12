import cv2
import numpy as np
import os


def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/2.jpg")

    B, G, R = cv2.split(img) #it splites the image into each color index

    print(B.shape)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    merged = cv2.merge([B,G,R])
    cv2.imshow("Merged", merged)

    merged = cv2.merge([B+100,G,R])
    cv2.imshow("Merged with Blue Amplified", merged)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()