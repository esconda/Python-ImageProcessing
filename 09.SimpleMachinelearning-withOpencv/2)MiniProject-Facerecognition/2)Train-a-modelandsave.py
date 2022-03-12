import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import os

# Get the training data we previously made
data_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.join(os.getcwd(), os.listdir(os.getcwd())[0]))))\
            +'/Master OpenCV/faces/user/'
onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

# Create arrays for training data and labels
Training_Data, Labels = [], []
# Open training images in our datapath
# Create a numpy array for training data
for i, files in enumerate(onlyfiles):
    if isfile(data_path+files):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        print(onlyfiles[i])
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(int(onlyfiles[i].split('-')[1].split('.')[0])) #Get specified label from image name,images should be image1-1,"-1" part represent "burak" name class,image1-2,"-2" part represent "furkan" name class

print(Labels)
# Create a numpy array for both training data and labels
Labels = np.asarray(Labels, dtype=np.int32)

# Initialize facial recognizer
model = cv2.face.LBPHFaceRecognizer_create()
# NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

# Let's train our model
model.train(np.asarray(Training_Data), np.asarray(Labels))
model.write(os.getcwd()+'/trainedfacemodel.yml')
model.write(os.getcwd()+'/trainedfacemodel.xml')
print("Model trained sucessefully")