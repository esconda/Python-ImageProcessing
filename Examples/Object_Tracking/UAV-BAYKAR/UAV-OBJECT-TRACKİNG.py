import numpy as np
import cv2 as cv
import time
import os

cam_cap = 0
fourcc = 0
cam_width = 0
cam_height = 0
target_start_point = 0
target_end_point = 0
target_init_boundingb = None
video_output = 0


def do_vid_config():
    global cam_cap
    cam_cap = cv.VideoCapture('D:/Tutorials/Python-Tutorials/Python_Opencv-Tutorials-Examples/Object_Tracking/UAV-BAYKAR/Baykartb2.mp4')
    #fourcc = cv.VideoWriter_fourcc('XVID')

    video_output = cv.VideoWriter('C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/2)Videoread&Videowrite(Camera)/output.avi',fourcc, 30.0, (int(cam_cap.get(3)), int(cam_cap.get(4))))

def main():
    global target_start_point
    global target_end_point
    global target_init_boundingb
    do_vid_config()

    tracker = cv.TrackerCSRT_create()

    while(cam_cap.isOpened()):
        ret,frame = cam_cap.read()
        cam_height = frame.shape[0]
        cam_width = frame.shape[1]
        target_start_point=  (cam_width//2-60,cam_height//2-60)
        target_end_point = (cam_width//2+60,cam_height//2+60)

        if frame is None:
            break

        if ret==True:

            if target_init_boundingb is not None:
                (success, box) = tracker.update(frame)
                # check to see if the tracking was a success
                if success:
                    (x, y, w, h) = [int(v) for v in box]
                    print("Box point in frame",(x+w/2), "x" , (y+h/2))
                    cv.rectangle(frame, (x, y), (x + w, y + h),
                                  (0, 255, 0), 2)


            cv.line(frame, (cam_width // 2-10, cam_height // 2), (cam_width // 2 - 40, cam_height // 2), (255, 255, 0), 2)
            cv.line(frame, (cam_width // 2+10, cam_height // 2), (cam_width // 2 + 40, cam_height // 2), (255, 255, 0), 2)
            cv.rectangle(frame, target_start_point, target_end_point, (0, 0, 255), 2)

            cv.imshow("Baykar",frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            #Look for re init operation of trackingq
            elif cv.waitKey(1) & 0xFF == ord("s"):
                target_init_boundingb = cv.selectROI("Frame", frame, fromCenter=False,
                                       showCrosshair=False)
                #target_init_boundingb =(20,30,40,60)

                #targetpic= frame[int(target_init_boundingb[1]):int(target_init_boundingb[1]+target_init_boundingb[3]), int(target_init_boundingb[0]):int(target_init_boundingb[0]+target_init_boundingb[2])]
                tracker.init(frame,target_init_boundingb)



        else:
            break



if __name__ =='__main__':
    main()