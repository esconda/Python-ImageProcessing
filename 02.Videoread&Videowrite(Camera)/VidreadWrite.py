# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:44:08 2019

@author: PM_br
"""
import cv2
import numpy as np
#Read from videofile and use videowriter to save
def main():
    cap_cam = cv2.VideoCapture('D:/Tutorials/Python-Tutorials/Python_Opencv-Tutorials-Examples/2)Videoread&Videowrite(Camera)/output.avi')#read frame from videocapture
    fourcc = cv2.VideoWriter_fourcc(*'XVID')#it can be also 'MJPG'
    
    #Where to save file and width height also fps
    video_output = cv2.VideoWriter('D:/Tutorials/Python-Tutorials/Python_Opencv-Tutorials-Examples/2)Videoread&Videowrite(Camera)/output1.avi',fourcc,5.0,(int(cap_cam.get(3)),int(cap_cam.get(4))))



    while(cap_cam.isOpened()):
        ret,frame = cap_cam.read() # read frame from cam
        height = frame.shape[0]
        width = frame.shape[1]

        if ret==True:
            video_output.write(frame)#write each frame from cam to videofile
            cv2.line(frame,(width//2,height//2),(width//2+300,height//2),(255,0,0),5)
            cv2.imshow("My_image", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap_cam.release()
    video_output.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()