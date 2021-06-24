import cv2
import numpy as np
import os
import time 



from os import listdir
from os.path import isfile, join


def face_detector(img, size=0.5):
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')    
    # Convert image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    if faces is ():
        return img, []
    
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,),2)
        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (200, 200))
    return img, roi

def modeltrainer():
    data_path = 'C:/Users/juzer/Desktop/summerprogram/CV/task5/faces/user/'
    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    # Create arrays for training data and labels
    Training_Data, Labels = [], []

    # Open training images in our datapath
    # Create a numpy array for training data
    for i, files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)

    # Create a numpy array for both training data and labels
    Labels = np.asarray(Labels, dtype=np.int32)


    juzer_model  = cv2.face_LBPHFaceRecognizer.create()
    # Let's train our model 
    juzer_model.train(np.asarray(Training_Data), np.asarray(Labels))
    print("Model trained sucessefully")
    return juzer_model

def user2modeltrainer():
    data_path = 'C:/Users/juzer/Desktop/summerprogram/CV/task5/faces/user2/'
    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    # Create arrays for training data and labels
    Training_Data, Labels = [], []

    # Open training images in our datapath
# Create a numpy array for training data
    for i, files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)

    # Create a numpy array for both training data and labels
    Labels = np.asarray(Labels, dtype=np.int32)


    user2_model  = cv2.face_LBPHFaceRecognizer.create()
    # Let's train our model 
    user2_model.train(np.asarray(Training_Data), np.asarray(Labels))
    print("Model trained sucessefully")
    return user2_model
