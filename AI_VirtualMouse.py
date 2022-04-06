import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy

####################
wCam, hCam=648, 488
####################

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

while True:
    success,img=cap.read()


    cTime= time.time()
    fps= 1/ (cTime -pTime)
    pTime = cTime
    cv2.putText(img,str(int(fps)),(20,50) ,cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0),3)

    cv2.imshow('webcam', img)
    cv2.waitKey(1)