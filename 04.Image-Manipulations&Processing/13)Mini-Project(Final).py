import cv2
import numpy as np
import matplotlib.pyplot as plt


def sketch(img):
    if img.shape[0]>0 and img.shape[1]>0:

        #Convert image to grayscale
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        #Clean up image using Gaussian Blur
        img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)

        #Extract Edges
        canny_edges = cv2.Canny(img_gray_blur,10,70)

        #Do an invert binarize the image
        ret,mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)

    else:
        print("Unfortunately Image is empty")
    return mask

def main():

    cap = cv2.VideoCapture(0)

    while True:
        ret,frame = cap.read()

        cv2.imshow('Live sketcher', sketch(frame))

        if cv2.waitKey(1) & 0xFF == 13: #13 is enter key
            cap.release()
            frame.release()
            cv2.destroyAllWindows()
            break



if __name__=='__main__':
    main()