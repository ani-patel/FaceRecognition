import cv2
import math

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)
Nose = cv2.CascadeClassifier('Nose.xml')
Eyes = cv2.CascadeClassifier('haarcascade_eye.xml')
Mouth = cv2.CascadeClassifier('Mouth.xml')
lex = 0
ley = 0
rex = 0
rey = 0
nx = 0
ny = 0
mx = 0
my = 0
count = 0
tbe = 0
tbren = 0
tblen = 0
tbrem = 0
tblem = 0
tbmn = 0
X1 = 0
Y1 = 0
X2 = 0
Y2 = 0
X3 = 0
Y3 = 0
X4 = 0
Y4 = 0
MY = 0
while(1):
    ret, Frame = cap.read()
    gray = cv2.cvtColor(Frame,cv2.COLOR_BGR2GRAY)
    facesInInputImage = face_cascade.detectMultiScale(gray, 1.3,10)
    for (x, y, w, h) in facesInInputImage:
        gray = gray[y:y+h, x:x+w]
        faceimg = Frame[y:y+h, x:x+w]
        faceimg = cv2.resize(faceimg, (500,500), interpolation=cv2.INTER_CUBIC)
        gray = cv2.resize(gray, (500, 500), interpolation = cv2.INTER_CUBIC)

        nosesInInputImage = Nose.detectMultiScale(gray, 1.5, minNeighbors = 3)
        for (x,y,w,h) in nosesInInputImage:
            nx = x + (w/2)
            ny = y + (h/2)
            if w > 100 and h > 50 and nx > 150 and nx < 350 and ny > 200 and ny < 350:
                noseimg = faceimg[y:y+h, x:x+w]
                cv2.circle(gray,(nx,ny), 10, (0,0,255), -1)
        eyesInInputImage = Eyes.detectMultiScale(gray)
        for (x,y,w,h) in eyesInInputImage:
            if w > 100 and h > 100 and w < 150 and h < 150:
                if x < 200:
                    lex = x + (w/2)
                    ley = y + (h/2)
                    X1 = x
                    Y1 = y
                    X2 = x
                    Y2 = y + h
                    cv2.circle(gray,(lex,ley),10,(255,0,0),-1)
                if (x + w) > 300:
                    rex = x + (w/2)
                    rey = y + (h/2)
                    X3 = x + w
                    Y3 = y
                    X4 = x + w
                    Y4 = y + h
                    cv2.circle(gray,(rex,rey),10,(255,0,0),-1)
        mouthsInInputImage = Mouth.detectMultiScale(gray, 1.5, minNeighbors = 6)
        for (x,y,w,h) in mouthsInInputImage:
            mx = x + (w/2)
            my = y + (h/2)
            if y > 250 and w > 100:
                mouthimg = faceimg[y:y+h,x:x+w]
                MY = y + h
                cv2.circle(gray,(mx,my),10,(255,0,0),-1)

    if lex != 0 and ley != 0 and rex != 0 and rey != 0 and nx != 0 and ny != 0 and mx != 0 and my != 0:
        betweeneyes = math.sqrt(math.pow(abs(rex - lex),2) + math.pow(abs(rey - ley),2))
        betweenrighteyenose = math.sqrt(math.pow(abs(rex - nx),2) + math.pow(abs(rey - ny),2))
        betweenlefteyenose = math.sqrt(math.pow(abs(lex - nx),2) + math.pow(abs(ley - ny),2))
        betweenrighteyemouth = math.sqrt(math.pow(abs(rex - mx),2) + math.pow(abs(rey - my),2))
        betweenlefteyemouth = math.sqrt(math.pow(abs(lex - mx),2) + math.pow(abs(ley - my),2))
        betweenmouthnose = math.sqrt(math.pow(abs(mx - nx),2) + math.pow(abs(my - ny),2))
        count = count + 1
        tbe = tbe + betweeneyes
        tbren = tbren + betweenrighteyenose
        tblen = tblen + betweenlefteyenose
        tbrem = tbrem + betweenrighteyemouth
        tblem = tblem + betweenlefteyemouth
        tbmn = tbmn + betweenmouthnose
        lex = 0
        ley = 0
        rex = 0
        rey = 0
        nx = 0
        ny = 0
        mx = 0
        my = 0
        if Y1 > Y3:
            X = X1
            Y = Y3
            W = X3 - X1
            H = Y2 - Y3
        else:
            X = X1
            Y = Y1
            W = X3 - X1
            H = Y4 - Y1
        eyesimg = faceimg[Y:Y+H,X:X+W]
        exactfaceimg = faceimg[Y:MY,X:X+W]
        cv2.imwrite('./faces/'+str(count)+'.jpg',exactfaceimg)
        cv2.imshow('Video', gray)
    if cv2.waitKey(1) == 1048603:
			break
    if count == 10:
        break
    cv2.imshow('Camera',Frame)

tbe = tbe/50
tbren = tbren/50
tblen = tblen/50
tbrem = tbrem/50
tblem = tblem/50
tbmn = tbmn/50

print tbe, tbren, tblen, tbrem, tblem, tbmn
cap.release()
cv2.destroyAllWindows()
