import cv2
import numpy as np
import os


def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/2.jpg")

    if img is None:
        print("Given path is wrong")

    while not img is None:
        cv2.imshow("My image", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # instead of ord you can put 27 which means esc key to exit
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()