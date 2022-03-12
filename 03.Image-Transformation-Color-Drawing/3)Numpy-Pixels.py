import cv2
import numpy as np
import os


def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")

    B, G, R = cv2.split(img) #it splites the image into each color index AND İT DOES NOT SHOW B ,G ,R WİTHOUT MERGE FUNCTION

    zeros = np.zeros(img.shape[:2], dtype=np.uint8)
    print(zeros.shape)

    cv2.imshow("RED", cv2.merge([zeros, zeros, R]))
    cv2.imshow("GREEN : ", cv2.merge([zeros, G, zeros]))
    cv2.imshow("BLUE : ", cv2.merge([B, zeros, zeros]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()