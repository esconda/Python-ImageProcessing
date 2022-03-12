import cv2
import imutils
import datetime
import time
import numpy as np
import os
import time
import json
def main():
    cap_cam = cv2.VideoCapture(0)  # read frame from cam
    cap_cam.set(3, 6401)
    cap_cam.set(4, 4800)
    #cap_cam1 = cv2.VideoCapture(0)  # read frame from cam
    data = {}
    cam_feature = {}

    cam_feature['Kamera Ozellikleri'] = []
    data['Frame basina gecen zaman'] = []

    width = cap_cam.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = cap_cam.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
    fps = cap_cam.get(cv2.CAP_PROP_FPS)

    cam_feature['Kamera Ozellikleri'].append(str(width) + " X " + str(height) + " FPS :" + str(fps))
    # loop over the frames of the video
    firstFrame = None
    while (cap_cam.isOpened()):
        # grab the current frame and initialize the occupied/unoccupied
        # text
        starttime = time.time()
        ret, frame = cap_cam.read()


        # if the frame could not be grabbed, then we have reached the end
        # of the video
        if frame is None:
            break

        # resize the frame, convert it to grayscale, and blur it
        #frame = imutils.resize(frame, width=500)
        starttime = time.time()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # if the first frame is None, initialize it
        if firstFrame is None:
            firstFrame = gray
            continue

        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        # dilate the thresholded image to fill in holes, then find contours
        # on thresholded image
        thresh = cv2.dilate(thresh, None, iterations=10)
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        elapsedtime = time.time()-starttime

        data['Frame basina gecen zaman'].append(str(elapsedtime*1000))
        print(elapsedtime*1000)
        # loop over the contours
        for c in cnts:
            # if the contour is too small, ignore it
            #if cv2.contourArea(c) < 200:
                #continue

            # compute the bounding box for the contour, draw it on the frame,
            # and update the text
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.putText(frame, "HAREKET ALGILANDI", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(frame, str(width) +' X '+str(height) + " "+ "FPS : "+ str(fps), (int(width-350), int(height-10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            # show the frame and record if the user presses a key
            cv2.imshow("MOTION DETECTION BY BURAK DOGANCAY", frame)
            #cv2.imshow("ABSORBATION FILTER GOSTERIMI", thresh)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            with open('data.txt', 'w') as outfile:
                json.dump(cam_feature,outfile)
                json.dump(data, outfile)
            break



if __name__ == '__main__':
    main()