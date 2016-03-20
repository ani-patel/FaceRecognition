import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

input_image = cv2.imread('eye.jpg',0)
eyes = eye_cascade.detectMultiScale(input_image)
print eyes
for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(input_image,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('eyes',input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()