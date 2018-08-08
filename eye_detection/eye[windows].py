import pyautogui
import cv2            
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')
	
cap=cv2.VideoCapture(0)
	
while True:
	ret,img=cap.read()
	gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.1 ,5)#1.5,5 1.3
	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
		roi_gray=gray[y:y+h, x:x+w] 
		roi_color=img[y:y+h, x:x+w] 
		eyes=eye_cascade.detectMultiScale(roi_gray)
		print(len(eyes))   
		if len(eyes)<2:
			pass
			pyautogui.press("space")
		for(ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	cv2.imshow('img',img)
	k=cv2.waitKey(30) & 0xff
	if k==27:
		break
cap.release()
cap.destroyAllWindows()

