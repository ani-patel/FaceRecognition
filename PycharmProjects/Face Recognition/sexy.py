import numpy as np
import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('ojoD.xml')
count = 0
while(1):
 ret, Frame = cap.read()
 gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
 #input_image1 = input_image
 input_image = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)

 facesInInputImage = face_cascade.detectMultiScale(input_image, 1.3, 10)
 for (x, y, w, h) in facesInInputImage:
        input_image = input_image[y:y+h, x:x+w]
        input_image = cv2.resize(input_image, (400, 400), interpolation = cv2.INTER_CUBIC)
        #eyes = eye_cascade.detectMultiScale(input_image)
        #for (ex,ey,ew,eh) in eyes:
        #    area = ew*eh
        #    if area > 1000 and area < 15000:
        #        cv2.rectangle(input_image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        #        print ew, eh
        mouth = mouth_cascade.detectMultiScale(input_image)
        for (ex,ey,ew,eh) in mouth:
            cv2.rectangle(input_image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('Video', input_image)
        count = count+1
        if cv2.waitKey(1) == 1048603:
			break
 if count == 50:
		break


cap.release()