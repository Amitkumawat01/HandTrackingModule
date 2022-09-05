import cv2
import mediapipe as mp
import  time
import HandTrackingModule as hmt
import math
import numpy as np
import pycaw

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
minVolume,maxVolume,avoid = volume.GetVolumeRange()

def distance(a,b):
    return math.sqrt((a[1]-b[1])**2+(a[2]-b[2])**2)

wcam,hcam = 640,480

cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
pTime=0
cTime=0
length=0

detecter = hmt.handDetector()

while True:
    success,img = cap.read()
    img = cv2.flip(img, 1)
    detecter.findHands(img)
    lmList = detecter.findPosition(img,draw=False,id=[4,6,8,12])

    if len(lmList) != 0:
        length = int(distance(lmList[0], lmList[3]))
        if length<=50 :
            volume.SetMasterVolumeLevel(-96.00, None)
            cv2.putText(img, f'Vol: {0}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 50<length and length<=70 :
            volume.SetMasterVolumeLevel(-34.75, None)
            cv2.putText(img, f'Vol: {10}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 70<length and length<=90 :
            volume.SetMasterVolumeLevel(-24.35, None)
            cv2.putText(img, f'Vol: {20}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 90<length and length<=110 :
            volume.SetMasterVolumeLevel(-18.24, None)
            cv2.putText(img, f'Vol: {30}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 110<length and length<=130 :
            volume.SetMasterVolumeLevel(-13.88, None)
            cv2.putText(img, f'Vol: {40}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 130<length and length<=150 :
            volume.SetMasterVolumeLevel(-10.50, None)
            cv2.putText(img, f'Vol: {50}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 150<length and length<=170 :
            volume.SetMasterVolumeLevel(-7.75, None)
            cv2.putText(img, f'Vol: {60}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 170<length and length<=190 :
            volume.SetMasterVolumeLevel(-5.41, None)
            cv2.putText(img, f'Vol: {70}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 190<length and length<=210 :
            volume.SetMasterVolumeLevel(-3.38, None)
            cv2.putText(img, f'Vol: {80}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 210<length and length<=230 :
            volume.SetMasterVolumeLevel(-1.60, None)
            cv2.putText(img, f'Vol: {90}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)
        elif 230<length :
            volume.SetMasterVolumeLevel(0.00, None)
            cv2.putText(img, f'Vol: {100}%', (5, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)


    cTime=time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime


    cv2.putText(img,f'FPS: {int(fps)}',(5,25),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
    # cv2.putText(img, f'Len: {int(length)}%', (5, 95), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

    cv2.imshow("Img",img)
    cv2.waitKey(1)

