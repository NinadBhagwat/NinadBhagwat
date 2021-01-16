# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:36:09 2021

@author: NINAD
"""
import cv2

face_cascade = cv2.CascadeClassifier(r"C:\Users\Admin\Desktop\face.xml")

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(127,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
    cv2.imshow('face_detection', img)
    k = cv2.waitKey(30)&0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()