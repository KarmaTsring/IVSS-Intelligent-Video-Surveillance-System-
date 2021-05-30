import cv2
import face_recognition
import numpy as np
import os
import time
from threading import Thread




class LoadImages(Thread):
    def __init__(self):
        pass

    def load_images(self):
        # path to the images
        path = '../../' + 'Images/Files'


        self.images = []
        self.peopleNames = []

        # declare temp to store imgs for certain loop
        temp = list()

        # decalre dirNames to record only name of subdir/images not entire relative path
        dirNames = list()
        subNames = []
        hemp = []

        self.dictionary = {}

        # as self.image occupies matrix data, need one list to store image for bounding box, name
        self.image_name = []

        myList = os.listdir(path)
        for dir, subdirs, files in os.walk(path):

            for subdirectory in subdirs:
                hemp = os.path.join(path, subdirectory)
                subNames.append(os.path.basename(hemp))

                # to get the multiple images from each respective person

                # from every for loop end, clear temp value to restore another
                temp = []

                self.peopleNames.append(os.path.splitext(subdirectory)[0])

            for imgs in files:
                # declare temp and join path between dir and imgs
                temp = os.path.join(path, imgs)

                # dirNames append to stores only the names but not relative path using os.path.basename()
                dirNames.append(os.path.basename(temp))

                # to read images one have to declare path in cv2.imread(path)

        # for keys in dict, use subnames
        for subdir in subNames:
            # declare empty list as values for all keys
            self.dictionary[subdir] = []

        # to proportionally store values containing 3 images in dict as values
        number = len(dirNames) / len(subNames)

        # conversion into int from float
        number = int(number)

        # point to loop through images
        point = 0

        # loop to store in dictionary
        for keys, values in self.dictionary.items():

            # loop to only 3 times as each personal image is stored
            for i in range(number):
                # to append in dictionary:list we use setdefault(key, default_value)
                self.dictionary.setdefault(keys, []).append(dirNames[point])

                # increment upto 3
                point += 1

        # to store read image using opencv cv2.imread
        for keys, values in self.dictionary.items():
            for img in values:
                # use curImg as current image
                curImg = cv2.imread(f'{path}/{keys}/{img}')

                self.images.append(curImg)
                self.image_name.append(img)

        print(self.peopleNames)

        return self.images


    def findEncodings(self):
        encodeList = []
        for img in self.load_images():
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)


        return encodeList

if __name__ == "__main__":
    load_image = LoadImages()
    load_image.load_images()