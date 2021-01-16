# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 11:08:54 2021

@author: NINAD
"""

import cv2
import numpy as np

face_classifier =cv2.CascadeClassifier(r'C:\Users\Admin\Desktop\face.xml')
eye_classifier  =cv2.CascadeClassifier(r'C:\Users\Admin\Desktop\eye.xml')

def face_detection(image):
    
    if ret is True:
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        faces=face_classifier.detectMultiScale(gray,1.6,7)

        for (x,y,w,h) in faces:
            
            cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),2)
            
            roi_color=image[y:y+h,x:x+w]
            roi_gray=gray[y:y+h,x:x+w]
            
            eyes=eye_classifier.detectMultiScale(roi_gray)
            
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
    
    return image
    
cap=cv2.VideoCapture(0)

while True:

    ret,frame=cap.read()
    cv2.imshow('face_detection',face_detection(frame))

    k = cv2.waitKey(30)&0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()