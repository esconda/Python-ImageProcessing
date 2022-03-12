import cv2
import numpy as np
import os


def main():

    cap = cv2.VideoCapture(0)
    mybool = True;
    while(cap.isOpened()):
        ret,frame = cap.read()
        if ret:
            cv2.imshow("My image", frame)
            if mybool:
                cv2.imwrite("Cam-Image.jpg",frame)
            if cv2.waitKey(1) & 0xFF == 27:  # instead of 27 you can put ord which means esc key to exit
                cv2.destroyAllWindows()
                break
        else:
            break
        mybool=False

if __name__ == '__main__':
    main()