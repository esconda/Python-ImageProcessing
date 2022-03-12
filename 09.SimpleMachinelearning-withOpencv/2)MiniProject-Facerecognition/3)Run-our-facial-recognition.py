import cv2
import numpy as np
import os

face_classifier = cv2.CascadeClassifier(os.path.dirname(os.path.dirname(os.path.dirname(os.path.join(os.getcwd(), os.listdir(os.getcwd())[0]))))
+'/Master OpenCV/Haarcascades/haarcascade_frontalface_default.xml')


def multiple_face_detector(img, size=0.5):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    print(len(faces))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        roi = img[y:y + h, x:x + w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

model = cv2.face.LBPHFaceRecognizer_create()
model.read(os.getcwd()+'/trainedfacemodel.xml')
Subjects = ["Burak","Furkan"]

# Open Webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    image, face = multiple_face_detector(frame)

    try:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        cv2.imshow("face",face)

        # Pass face to prediction model
        # "results" comprises of a tuple containing the label and the confidence value

        results = model.predict(face)
        print(results)
        if results[1] < 500:
            confidence = int(100 * (1 - ((results[1]) / 400)))
            display_string = str(confidence) + '% Confident it is ' + Subjects[results[0]-1]

        cv2.putText(image, display_string, (100, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 150), 2)

        if confidence > 75:
            cv2.putText(image, "Unlocked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow('Face Recognition', image)
        else:
            cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow('Face Recognition', image)

    except:
        cv2.putText(image, "No Face Found", (220, 120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.putText(image, "Locked", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Face Recognition', image)
        pass

    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

cap.release()
cv2.destroyAllWindows()