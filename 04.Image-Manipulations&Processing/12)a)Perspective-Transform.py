import cv2
import numpy as np
import os


# CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 31
#Warp affine geometric transformation according to coordinates
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/4.jpg", 0)
    cv2.imshow("Original", img)


    #Coordinates of the 4 corners of the original image
    points_A = np.float32([[150,15],[80,60],[60,100],[260,320]])

    #Coordinates of the 4 corners of the desired output
    #We use a ratio of an A4 Paper 1:1.41
    points_B = np.float32([[0,0], [200,10],[40,120],[30,140]])

    #Use the two sets of four points to compute
    #the perspective transformation matrix,M
    M = cv2.getPerspectiveTransform(points_A,points_B)

    warped = cv2.warpPerspective(img,M,(500,500))

    cv2.imshow('warpperspective',warped)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()