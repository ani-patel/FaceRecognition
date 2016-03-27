import cv2
img = cv2.imread('orl_faces/s1/1.pgm') # load a dummy image
cv2.imwrite('chutyapa.png',img)
while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(33)
    if k==27:    # Esc key to stop
        break
    elif k==-1:  # normally -1 returned,so don't print it
        continue
    else:
        print k # else print its value