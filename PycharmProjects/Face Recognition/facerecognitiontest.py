import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
count = 0
Nose = cv2.CascadeClassifier('Nose.xml')
Eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
Mouth = cv2.CascadeClassifier('Mouth.xml')

while(1):
    ret, Frame = cap.read()
    gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    facesInInputImage = face_cascade.detectMultiScale(gray, 1.3, 10)
    for (x, y, w, h) in facesInInputImage:
        gray = gray[y:y+h, x:x+w]
        gray = cv2.resize(gray, (500, 500), interpolation = cv2.INTER_CUBIC)
        count = count+1
        nosesInInputImage = Nose.detectMultiScale(gray, 1.5, minNeighbors = 3)
        for (x,y,w,h) in nosesInInputImage:
            if w > 100 and h > 50:
                cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)
        eyesInInputImage = Eyes.detectMultiScale(gray)
        eyescount = 0
        for (x,y,w,h) in eyesInInputImage:
            if w > 100 and h > 100 and w < 150 and h < 150:
                eyescount = eyescount + 1
                if x < 200:
                    lex = x + (w/2)
                    ley = y + (h/2)
                if (x + w) > 300:
                    rex = x + (w/2)
                    rey = y + (h/2)
        if eyescount == 2:
            cv2.line(gray,(lex,ley),(rex,rey),(255,0,0),5)
        mouthsInInputImage = Mouth.detectMultiScale(gray, 1.5, minNeighbors = 6)
        for (x,y,w,h) in mouthsInInputImage:
            if y > 250 and w > 100:
                cv2.rectangle(gray,(x,y),(x+w,y+h),(0,255,0),2)


        cv2.imshow('Video', gray)
    if count == 50:
        break
    if cv2.waitKey(1) == 1048603:
			break
    cv2.imshow('Camera',Frame)

cap.release()
cv2.destroyAllWindows()
