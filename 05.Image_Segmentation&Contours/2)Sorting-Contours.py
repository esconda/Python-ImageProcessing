import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def label_contour_center(img,c,i):
    #Places a red circle on the centers of contours
    M = cv2.moments(c)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])

    #Draw the contour number on the image
    cv2.circle(img,(cx,cy),10,(0,255,0),-1)
    return img

#It is sorting by position
def x_cord_contour(contours):
    if cv2.contourArea(contours):
        M = cv2.moments(contours)
        return int(M['m10']/M['m00'])
    else:
        print("nothing is available")

def get_contours_areas(contours):

    all_areas = []

    for cnt in contours:
        area = cv2.contourArea(cnt)
        all_areas.append(area)
    return all_areas

# CHECK FOR  34
# SORTING CONTOURS
def main():
    img = cv2.imread("D:/Tutorials/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/shapes1.jpg")
    cv2.imshow("1)Original", img)

    blank_image = np.zeros((img.shape[0],img.shape[1],3))

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find Canny Edges
    edged = cv2.Canny(img_gray, 10, 100)
    cv2.imshow("2)Canny Edges", edged)

    # Finding Contours
    # Use copy of our image, since findcontours alters the image
    contoursimg = edged.copy()

    contours, hierarchy = cv2.findContours(contoursimg, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('3)Canny edges after contourng', contoursimg)
    print("Number of Contours found =" + str(len(contours)))
    print("contours", contours[0])


    # for i,c in enumerate(contours):
    # area = cv2.contourArea(1)

    # Draw all contours
    # Use '-1' as the 3rd parameter to draw all
    cv2.drawContours(blank_image, contours, -1, (0, 255, 0), 3)
    cv2.imshow(("4)All contours on blank image"), blank_image)

    cv2.imshow('5)Contours on image', img)

    # -------SORTING CONTOURS-----------
    #Sort contours large to small
    sorted_contours = sorted(contours, key= cv2.contourArea, reverse = True)

    print("Contours area after sorting",get_contours_areas(sorted_contours))

    #Iterate over our contours and draw one at a time
    for c in sorted_contours:
        cv2.drawContours(img,[c],-1,(0,0,255),3)
        cv2.imshow('6)Contours by area',img)
    #----------------------------------


    #------Computer Center of Mass or centroids and draw them on our image------
    for (i,c) in enumerate(contours):
        orig = label_contour_center(img,c,i)
        cv2.imshow("7)Contours Center",orig)
    #----------------------------------



    #-------- LABELING CONTOURS LEFT TO RİGHT----------
    #Sort by left to right using our x_coord_contour function
    contours_left_to_right = sorted(contours, key=cv2.contourArea, reverse=False)

    print("Sorted from min to max value",get_contours_areas(contours_left_to_right))
    for (i,c) in enumerate(contours_left_to_right):
        cv2.drawContours(img,[c],-1,(0,255,255),3)
        M= cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        cv2.putText(img,str(i+1),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow("8)Left to right contour",img)
    #------------------------------------------------------


        #----------BOUNDING RECT AND CROP IMAGE------
        (x,y,w,h) = cv2.boundingRect(c)
        croppedimg = img[y:y + h, x:x + w]
        cv2.imshow("Cropped Image" + str(i+1),croppedimg)
        cv2.waitKey(800)
        #----------------------------------------------
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()