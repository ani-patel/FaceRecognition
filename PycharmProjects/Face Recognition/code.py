
import cv2, os, sys
import numpy as np
from PIL import Image


def get_training_set(path):
	image_paths = [os.path.join(path, f) for f in os.listdir(path)]

	images = []
	labels = []
	for image_path in image_paths:

		image1 = cv2.imread(image_path)
		image = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
		label = int(image_path[19:21])
		images.append(image)
		labels.append(label)

	return images, labels 


def label_to_name(label, confidence):
	if label == 1:
			print "Indranil is detected with confidence {}".format(confidence)
	elif label == 2:
			print "Aniket is detected with confidence {}".format(confidence)
	elif label == 3:
			print "Shubhankar is detected with confidence {}".format(confidence)
	elif label == 4:
			print "Suraj is detected with confidence {}".format(confidence)
	elif label == 5:
			print "Sagar is detected with confidence {}".format(confidence)
	elif label == 6:
			print "Hussain is detected with confidence {}".format(confidence)
	return

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

face_recognizer = cv2.createLBPHFaceRecognizer()

images, labels = get_training_set('./finalsss')

face_recognizer.train(images, np.array(labels))

'''input_image = cv2.imread(sys.argv[1])
height, width, c = input_image.shape
input_image = cv2.resize(input_image, (width/2, height/2), interpolation = cv2.INTER_CUBIC)'''
cap = cv2.VideoCapture(0)
count = 0
while(1):
 ret, Frame = cap.read()
 gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
 #input_image1 = input_image
 input_image = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
 facesInInputImage = face_cascade.detectMultiScale(input_image, 1.3, 10)
 for (x, y, w, h) in facesInInputImage:
		input_image = input_image[y:y+h, x:x+w]
		input_image = cv2.resize(input_image, (200, 200), interpolation = cv2.INTER_CUBIC)
		#labelDetected, confidence = face_recognizer.predict(input_image)
		#cv2.rectangle(input_image, (x, y), (x+w, y+h), (0,255,0), 3)
		#print labelDetected
		#label_to_name(labelDetected, confidence)
		cv2.imshow('Video', input_image)
		count = count+1
		if cv2.waitKey(1) == 1048603:
			break
 if count == 50:
		break

cap.release()

'''input_image1 = input_image
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
facesInInputImage = face_cascade.detectMultiScale(input_image, 1.3, 10)

#for (x, y, w, h) in facesInInputImage:
#		input_image = input_image[y:y+h, x:x+w]
input_image = cv2.resize(input_image, (200, 200), interpolation = cv2.INTER_CUBIC)
labelDetected, confidence = face_recognizer.predict(input_image)
print labelDetected
#cv2.rectangle(input_image1, (x, y), (x+w, y+h), (0,255,0), 3)
label_to_name(labelDetected, confidence)

cv2.imshow('image', input_image1)

cv2.waitKey(0)'''

cv2.destroyAllWindows()








		
