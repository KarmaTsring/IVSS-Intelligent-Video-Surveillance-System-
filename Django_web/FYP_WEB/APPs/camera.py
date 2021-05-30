import cv2
import face_recognition
import numpy as np
import os
import time
from threading import Thread
from .Load_images_encodings import LoadImages
import winsound



class FaceRecognition(object):
    def __init__(self,name='camer_buffer_cleaner_thread'):
        self.video = cv2.VideoCapture(0)



        #Initialize the loadimages class to call methods
        self.load_images = LoadImages()


        self.encodeListKnown = self.load_images.findEncodings()




    def __del__(self):
        self.video.release()


    def getFrame(self):

        #encodeListKnown = self.load_images.findEncodings()
        # initializing video stream from device camera :0

        success, self.frame = self.video.read()

        # gray scale images if success

        imgSml = cv2.resize(self.frame, (0, 0), fx=0.33, fy=0.33)
        imgSml = cv2.cvtColor(imgSml, cv2.COLOR_BGR2RGB)

        #fps of video
        fps = self.video.get(cv2.CAP_PROP_FPS)
        fps = str(fps)


        cv2.putText(self.frame, f'FPS: {fps}', (0,70),cv2.FONT_HERSHEY_SIMPLEX , 0.5, (100, 255,0), 3, 1)

        facesCurFrame = face_recognition.face_locations(imgSml)
        encodeCurFrame = face_recognition.face_encodings(imgSml, facesCurFrame, num_jitters=1, model='small')

        def bounding_boxes(name, status, rgb):
            # due to faceLoc rule of faceLoc(height,top,bottom,left)
            y, w, h, x = faceLoc
            y, w, h, x = y*3, w*3, h*3, x*3
            cv2.rectangle(self.frame, (x, y), (w, h), (120, 120, 0), 1)
            cv2.rectangle(self.frame, (x, h - 25), (w + 100, h), rgb, cv2.FILLED)
            cv2.putText(self.frame, status, (x + 6, y - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (rgb), 1)
            cv2.putText(self.frame, name, (x + 6, h - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

        for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace, tolerance=0.44)
            name = "unknown"

            faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
            print(faceDis)

            # lowest match index
            matchIndex = np.argmin(faceDis)

            #to get the closest matching image
            #error
            matched_image = self.load_images.image_name[matchIndex]

            if matches[matchIndex]:
                for keys, values in self.load_images.dictionary.items():
                    if matched_image in values:

                        name = keys.upper()
                        print(name)

                        splitted = name.split('_')
                        if (splitted[1] == 'CUSTOMER'):
                            bounding_boxes(splitted[0], 'Customer', (0, 255, 0))
                        if (splitted[1] == 'OFFENDER'):
                            bounding_boxes(splitted[0], 'Known Offender', (0,0,255))
                            winsound.Beep(500, 250)

                        if (splitted[1] == 'STAFF'):
                            bounding_boxes(splitted[0], 'Staff', (241, 146, 241))

            if name == 'unknown':
                bounding_boxes(name, 'Un identified', (0, 0, 255))

        #resize = cv2.resize(self.frame, (640, 480), interpolation = cv2.INTER_LINEAR)
        ret, jpeg = cv2.imencode('.jpeg', self.frame)
        return jpeg.tobytes()






if __name__ == '__main__':
    #Make a game instance, and run the game

    while True:
        try:
            faceRecog = FaceRecognition()
            #faceRecog.getFrame()
        except AttributeError:
            pass








