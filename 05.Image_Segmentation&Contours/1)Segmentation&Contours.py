import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# CHECK FOR BEST RESIZING METHODS FROM TUTORIAL 33
# CONTOURS
def main():
    img = cv2.imread("D:/Tutorials/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/shapes1.jpg")
    cv2.imshow("Original", img)

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Find Canny Edges
    edged = cv2.Canny(img_gray,30,200)
    cv2.imshow("Canny Edges",edged)

    #Finding Contours
    #Use copy of our image, since findcontours alters the image
    contoursimg = edged.copy()
    contours,hierarchy = cv2.findContours(contoursimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.imshow('Canny edges after contourng',contoursimg)
    print("Number of Contours found =" + str(len(contours)))
    print("contours", contours[0])


    #cv2.CHAIN_APPROX_NONE stores all the boundary points.But we dont need all
    #bounding points
    #cv2.CHAIN_APPROX_SIMPLE instead only provide these start and end points of
    #bounding contours

    #
    #cv2.RETR_LIST - Retrieves all contours
    #cv2.RETR_EXTERNAL - Retrieves external or outer contours only
    #cv2.RETR_COMP - Retrieves all in a 2-level hierarchy
    #cv2.RETR_TREE - rETRİEVES ALL İN FULL HİERARCHY

    # for i,c in enumerate(contours):
    #area = cv2.contourArea(1)

    #Draw all contours
    #Use '-1' as the 3rd parameter to draw all
    cv2.drawContours(img,contours, -1, (0,255,0), 3)

    cv2.imshow('Contours', img)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()