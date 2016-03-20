import numpy as np
import cv2

for i in xrange(10):
	filename = './finalsss/subject_03_'+str(i+1)+'.bmp'
	print filename
	img = cv2.imread(filename,0)
	print img
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	img = clahe.apply(img)
	#img = cv2.imread('haha.jpg',0)
	#img = cv2.resize(img, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
	laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize = 3)	
	blur = cv2.GaussianBlur(laplacian, (5,5), 0)
	#ret, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	ret, binary = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
	kernel = np.ones((3,3),np.uint8)
	#th = cv2.dilate(binary, kernel, iterations = 2)
	#th = cv2.erode(th, kernel, iterations = 2)
	contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	area = 15
	for i in contours:
		if cv2.contourArea(i) > area:
			cv2.drawContours(img, [i], 0, (0,255,0), 3)
	cv2.imshow('image',blur)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
