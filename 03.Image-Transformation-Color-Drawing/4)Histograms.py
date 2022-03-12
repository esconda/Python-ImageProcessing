import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

#need matplotlib to create our histogram plots
def main():
    img = cv2.imread("C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Images/3.jpg")
    histogram = cv2.calcHist([img], [0], None , [256], [0,256])

    #We plot a histogram , ravel() flatens our image array
    print(img.ravel().shape)
    plt.hist(img.ravel(), 256,[0,256]); plt.show()

    #Viewing speprate color channels
    color = ('b','g','r')

    #we now seperate the colors and plot each in histograms
    for i, col in enumerate(color):
        histogram2 = cv2.calcHist([img],[i],None,[256], [0,256])
        plt.plot(histogram2,color=col)
        plt.xlim([0,256])

    plt.show()

if __name__ == '__main__':
    main()