import numpy as np
import cv2

for i in xrange(10):
	filename = 'orl_faces/s5/'+str(i+1)+'.pgm'
	print filename
	img = cv2.imread(filename,0)
	#img = cv2.imread('haha.jpg',0)
	img = cv2.resize(img, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
	img2 = img.copy()
	laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize = 3)	
	blur = cv2.GaussianBlur(laplacian, (5,5), 0)
	ret, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	#ret, binary = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
	contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	kernel = np.ones((3,3),np.uint8)
	for c in contours:
		if cv2.contourArea(c) > 10:
			cv2.drawContours(img,[c],0,(0,255,0),3)
			ret, binary = cv2.threshold(img,0,255,cv2.THRESH_BINARY)
			binary = cv2.erode(binary,kernel,iterations=1)
	contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		if cv2.contourArea(c) > 100 and cv2.contourArea(c) < 2000:
			M = cv2.moments(c)
			cx = int(M['m10']/M['m00'])
			cv2.drawContours(img2,[c],0,(0,255,0),3)

	cv2.imshow('image',img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
