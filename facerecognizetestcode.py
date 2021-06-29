import sys
import cv2
import numpy as np
import face_recognition as fr
import os
from datetime import datetime
import winsound
import requests
import json
from threading import Thread
path="ImageSimpleTest"
import requests
images=[]
imageClass=[]
mylist=os.listdir(path)
for person in mylist:
    folder=os.listdir(path+'/'+person)
    for cl in folder:
        cimage=cv2.imread(f'{path}/{person}/{cl}')
        images.append(cimage)
        imageClass.append(os.path.splitext(cl)[0])

print(imageClass)

def findencoding(images):
    encodinglist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encod=fr.face_encodings(img)[0]
        encodinglist.append(encod)
    return encodinglist

knownencoding=findencoding(images)
print(len(knownencoding))

def attandance(name):
    with open("presentlist.csv",'r+') as f:
        mydatalist=f.readlines()
        mylist=[]
        for l in mydatalist:
            dentr=l.split(',')
            mylist.append(dentr[0])
        if name not in mylist:
            now=datetime.now()
            dates=now.strftime("%m/%d/%Y, %H:%M:%S")
            f.writelines(f'\n{name}, {dates}')

#clockinclockout function

# def ClockInorOut(name):
#     getdata = requests.get("http://hrms.tforcehrms.com/admin/api/clockInOutState")
#     data = getdata.json()
#
#     # # # print(data)
#     container = []
#     for i in data:
#         # print(i)
#         if (i['employee_id'] == name):
#             container.append(i)
#     last_elem = container[-1]
#     current_clock_status = ""
#     post_url = "http://hrms.tforcehrms.com/admin/api/clockInOut"
#     clock_state=""
#     if (last_elem['clock_in'] != "" and last_elem['clock_out'] != ""):
#         clock_state="clock_in"
#     else:
#         clock_state = "clock_out"
#     post_data = {
#         "user_id": name,
#         "clock_state": clock_state,
#         "latitude": "1",
#         "longitude": "1",
#         "ip_address": "127.0.0.1"
#     }
#     response = requests.post(post_url, data=json.dumps(post_data))
#     print(response.json())

#initial webcame
webcam=cv2.VideoCapture(0)
name=""
while True:
    success,img=webcam.read()
    imgs=cv2.resize(img,(176, 144))
    imgs=cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
    facecloc=fr.face_locations(imgs)
    facecencod=fr.face_encodings(imgs,facecloc)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    faceName=[]
    for encode,facecloc in zip(facecencod,facecloc):
        matches=fr.compare_faces(knownencoding,encode)
        faceDis=fr.face_distance(knownencoding,encode)
        #finding maching index
        matcheIndex=np.argmin(faceDis)

        if matches[matcheIndex]:
            name=imageClass[matcheIndex].upper()
            y1,x2,y2,x1=facecloc
            y1, x2, y2, x1= y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),cv2.FILLED)

            cv2.putText(img,name,[x1+6,y2-6],cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)

            attandance(name)
            # ClockInorOut(name)


        else:
            winsound.PlaySound("alert.wav",winsound.SND_ASYNC)
    cv2.imshow("Rana's Phone Camera: ",img)

    cv2.waitKey(1)
cv2.destroyAllWindows()
