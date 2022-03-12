import cv2 as opencv
import numpy as np
import sys
import imutils


def difference_images(before,after):


    threshodl = 20
    difference = opencv.absdiff(before,after) #find difference between two image

    masking = opencv.cvtColor(difference,opencv.COLOR_BGR2GRAY) #convert difference to gary
    imask = masking>threshodl #find true values in masking image array

    #Fill canvas with zeros and then apply mask with tru values in matrix
    canvas = np.zeros_like(after,np.uint8)
    canvas[imask] = after[imask]

    #Apply thresholding to final image
    gray = opencv.cvtColor(canvas,opencv.COLOR_BGR2GRAY)
    ret,thresholded_image = opencv.threshold(gray,10,255,opencv.THRESH_BINARY)

    #Finding contours
    cnts = opencv.findContours(thresholded_image.copy(), opencv.RETR_EXTERNAL, opencv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = sorted(cnts, key=opencv.contourArea, reverse=True) #sort all the contours and set biggest contour to [0] index
    #h,w,ch = after.shape
    #print(w)

    for each in c:
        eachafter = each[0,0]

        # compute the rotated bounding box of the largest contour
        rect = opencv.minAreaRect(each)#The function calculates and returns the minimum-area bounding rectangle (possibly rotated) for a specified point set.
        box = opencv.cv.BoxPoints(rect) if imutils.is_cv2() else opencv.boxPoints(rect)
        box = np.int0(box)

        boxtextpoints=box[3,0]-box[0,0] #calculate width of the box

        print(boxtextpoints)

        # draw a bounding box arounded the detected difference object
        opencv.putText(after,"Object",(eachafter[0]- boxtextpoints,eachafter[1]-5) ,opencv.FONT_HERSHEY_SIMPLEX,0.6,(255,255,255),2,opencv.LINE_AA)
        opencv.drawContours(after, [box], -1, (0, 255, 0), 3)


    # opencv.imshow("Masking", masking)
    # opencv.imshow("my_image", canvas)
    # opencv.imshow("Convert final to gray", gray)
    # opencv.imshow("Thresholded", thresholded_image)
        opencv.imshow("image",after)
def main():
    beforeimg = opencv.imread("images/before.jpg")
    afterimg = opencv.imread("images/after.jpg")

    difference_images(beforeimg,afterimg)

    if opencv.waitKey(20000) == 27:
        sys.exit()

if __name__ =='__main__':
    main()