# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:20:48 2019

@author: PM_br
"""

import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    kernelforerode = np.ones((6,6),np.uint8)
    kernelfordialte = np.ones((5,5),np.uint8)
    while(1):
        # Take each frame
        _, frame = cap.read()
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([80,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        #Morphological filters
        #cv2.dilate(mask,kernel,mask) #extract white areas and make white areas bigger
        cv2.erode(mask,kernelforerode,mask)
        #cv2.dilate(mask,kernel,mask)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)
        
        
        cv2.imshow('frame',frame)
        cv2.imshow('HSV',hsv)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    
if __name__=='__main__':
    main()
