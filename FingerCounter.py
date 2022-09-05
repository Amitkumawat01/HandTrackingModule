import cv2
import mediapipe as md
import time
import HandTrackingModule as hmt

wcam,hcam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
pTime=0
cTime=0

detecter = hmt.handDetector()

while True:
    success,img = cap.read()
    img = cv2.flip(img, 1)
    detecter.findHands(img,draw=False)
    detecter.findPosition(img)

    fingers = detecter.fingersUp()
    fcount = sum(fingers)

    if len(fingers)!=0:
        cv2.putText(img, f'FingersUp: {fcount}', (5, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0),1)
        if fingers[0]:
            cv2.putText(img, f'Thumb: Up', (5, 110), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        else :
            cv2.putText(img, f'Thumb: Down', (5, 110), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        if fingers[1]:
            cv2.putText(img, f'Index F: Up', (5, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        else :
            cv2.putText(img, f'Index F: Down', (5, 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        if fingers[2]:
            cv2.putText(img, f'Middle F: Up', (5, 190), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        else :
            cv2.putText(img, f'Middle F: Down', (5, 190), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        if fingers[3]:
            cv2.putText(img, f'Ring F: Up', (5, 230), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        else :
            cv2.putText(img, f'Ring F: Down', (5, 230), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        if fingers[4]:
            cv2.putText(img, f'Pinky F: Up', (5, 270), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        else :
            cv2.putText(img, f'Pinky F: Down', (5, 270), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    cTime=time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img,f'FPS: {int(fps)}',(5,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)

    cv2.imshow("Img",img)
    cv2.waitKey(1)