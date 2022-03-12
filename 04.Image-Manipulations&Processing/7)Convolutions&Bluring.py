import cv2
import numpy as np
import os

#CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 26
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")

    #Creating Kernel
    kernel_3x3 = np.ones((3,3),np.float32)/9

    #We use the cv2.filterd2d to convolve the kernel with an image
    blurred = cv2.filter2D(img,-1,kernel_3x3)
    cv2.imshow("3x3 kernel blurring", blurred)
    cv2.waitKey(0)

    #Creating our 7x7 kernel
    kernel_7x7 = np.ones((7, 7), np.float32) / 49

    # We use the cv2.filterd2d to convolve the kernel with an image
    blurred2 = cv2.filter2D(img, -1, kernel_7x7)
    cv2.imshow("7x7 kernel blurring", blurred2)
    cv2.waitKey(0)

    #GAUSSIAN FILTER
    Gaussian = cv2.GaussianBlur(img, (7,7), 0)
    cv2.imshow("Gaussian blurring", Gaussian)
    cv2.waitKey(0)

    # BOX FILTER
    blur = cv2.blur(img, (3, 3))
    cv2.imshow("Averaging", blur)
    cv2.waitKey(0)

    # MEDIAN FILTER
    median = cv2.medianBlur(img, 5)
    cv2.imshow("Median Blur", median)
    cv2.waitKey(0)

    # Bilateral is very effective in noise removal while keepin edges sharp
    bilateral = cv2.bilateralFilter(img, 9,75,75)
    cv2.imshow("Bilateral Blur", bilateral)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()