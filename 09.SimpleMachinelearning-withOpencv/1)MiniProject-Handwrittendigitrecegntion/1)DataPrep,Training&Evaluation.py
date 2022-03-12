import numpy as np
import cv2

#JUST FOR MAKING CLASS PREDICTION,CALASSIFICATION NOT FOR REGRESSION OR FINDG BOX
# Let's take a look at our digits dataset
image = cv2.imread('C:/Users/PM_br/PycharmProjects/Python-Tutorials/Python_Opencv-Tutorials-Examples/Master OpenCV/images/digits.png')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
small = cv2.pyrDown(image)
cv2.imshow('Digits Image', image)

# Split the image to 5000 cells, each 20x20 size, means 5000 20x20 image
# This gives us a 4-dim array: 50 x 100 x 20 x 20
cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
print("Definitive cells",len(cells),len(cells[1]) )
print("Image height and width", image.shape[0], image.shape[1]) #Image shape is 1000 and 2000 , we should get 20x20 number image from this img with splitting by 50 and 100



# Convert the List data type to Numpy Array of shape (50,100,20,20)
x = np.array(cells)
print ("The shape of our cells array: " + str(x.shape))
cv2.imshow("Example Cells", x[1,2])
print("Example Cell Shape",x[1,2].shape)


# Split the full data set into two segments
# One will be used fro Training the model, the other as a test data set
train = x[:,:70].reshape(-1,400).astype(np.float32) # Size = (3500,400)#It will get first 50 row and 70 20x20 area , -1 means leave value as normal, 400 is for 20x20 text
test = x[:,70:100].reshape(-1,400).astype(np.float32) # Size = (1500,400)#It will get second 50 row and 30 20x20 area, -1 means leave value as normal, 400 is for 20x20 text
print("Train data out of 5000", train.shape)
print("Test data out of 5000", test.shape)


# Create labels for train and test data
k = [0,1,2,3,4,5,6,7,8,9]# Name all handwritten digits for kNearest operation
train_labels = np.repeat(k,350)[:,np.newaxis] #sırasıyla 350 şer 0,1,2,3,4,5,6,7,8,9 dikey eksende row olarak oluştutrur OLUŞTURUR
test_labels = np.repeat(k,150)[:,np.newaxis]
print("Train Labels :",train_labels.shape[1])
print("Train Labels data :",train_labels[349])
print("Test Labels :",test_labels)
cv2.waitKey(100000)

# Initiate kNN, train the data, then test it with test data for k=3
knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE, train_labels)
ret, result, neighbors, distance = knn.findNearest(test, k=3)

# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result == test_labels
correct = np.count_nonzero(matches)
accuracy = correct * (100.0 / result.size)
print("Accuracy is = %.2f" % accuracy + "%")