import cv2
import numpy as np
import os


def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")

    B,G,R = img[int(img.shape[0]/2),int(img.shape[1]/2)] #Middle point pixel values of image
    print("bgr value: ",B,G,R)
    print("image shape : ",img.shape)

    grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print("gray image pixel val: ",grey_img[0,20])

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    xyz_img = cv2.cvtColor(img,cv2.COLOR_BGR2XYZ)
    luv_img = cv2.cvtColor(img,cv2.COLOR_BGR2LUV)
    hls_img = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

    cv2.imshow("Normal Image", img)
    cv2.imshow("Grey Image",grey_img)

    #HSV IMAGES
    cv2.imshow("HSV Image", hsv_img)
    cv2.imshow("Hue Channel : ", hsv_img[:,:,0])
    cv2.imshow("Saturation Channel : ", hsv_img[:, :, 1])
    cv2.imshow("Value Channel : ", hsv_img[:, :, 2])

    cv2.imshow("RGB Image", rgb_img)
    cv2.imshow("xyz image",xyz_img)
    cv2.imshow("Luv image", luv_img)
    cv2.imshow("Hls image", hls_img)

    cv2.waitKey(10000)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()