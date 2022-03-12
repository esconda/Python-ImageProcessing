import cv2
import numpy as np
import os


def main():
    #Create black image
    image = np.zeros((512,512,3),np.uint8)

    #Can we make this in black and white
    image_bw = np.zeros((512,512),np.uint8)

    cv2.line(image,(0,0),(image.shape[0],image.shape[1]), (255,127,0), 5)
    cv2.rectangle(image,(40,40),(int(image.shape[0]/2),int(image.shape[1]/2)),(0,0,254),-1)
    cv2.circle(image,(70,70),100,(0,254,0),-1) # -1 is filling inside of rectangle
    cv2.putText(image,'Hello World',(75,290),cv2.FONT_HERSHEY_COMPLEX,2,(100,170,0), 3)
    #CHECK FOR POLYLINES

    cv2.imshow("Black Rectangle (Color)", image)
    cv2.imshow("Black Rectangle (B&W)", image_bw)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()