import cv2
import numpy as np
import os


def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")

    #Store height and width of the image
    height, width = img.shape[:2]

    quarter_height,quarter_width = height/4, width/4

    #    |1 0 Tx|
    # T =|0 1 Ty|
    #T is our translation matrix
    T = np.float32([[1,0,quarter_width],[0,1,quarter_height]])
    print(T)

    #Move image with quarter height and width
    img_translation = cv2.warpAffine(img, T, (width,height))
    cv2.imshow('Translation',img_translation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()