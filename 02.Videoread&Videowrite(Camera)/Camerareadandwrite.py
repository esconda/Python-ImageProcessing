# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 12:36:54 2019

@author: PM_br
"""
import cv2
import numpy as np

def main():
    cap_cam = cv2.VideoCapture(0)#read frame from cam
    fourcc = cv2.VideoWriter_fourcc(*'XVID')#it can be also 'MJPG'
    
    #Where to save file and width height also fps
    video_output = cv2.VideoWriter('C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/2)Videoread&Videowrite(Camera)/output.avi',fourcc,30.0,(int(cap_cam.get(3)),int(cap_cam.get(4))))
    
    while(cap_cam.isOpened()):
        ret,frame = cap_cam.read() # read frame from cam
        
        if ret==True:
            video_output.write(frame)#write each frame from cam to videofile
            
            cv2.imshow("My_image", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap_cam.release()
                video_output.release()
                cv2.destroyAllWindows()
                break
        else:
            break
        

if __name__=='__main__':
    main()