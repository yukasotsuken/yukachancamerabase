
import argparse
import datetime
import imutils
import math
import cv2
import numpy as np
import pyrebase

config = {
  "apiKey": "AIzaSyCC7DG-nDG7Qc3YzgUriicduohjQFd1qGE",
  "authDomain": "yukachan-ed770.firebaseapp.com",
  "databaseURL": "https://yukachan-ed770.firebaseio.com",
  "storageBucket": "yukachan-ed770.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("yuka@yukachan.com", "yukachan")
db = firebase.database()

width = 800

textIn = 0
textOut = 0

def testIntersectionIn(x, y):

    res = -450 * x + 400 * y + 157500
    if((res >= -550) and  (res < 550)):
        print (str(res))
        return True
    return False



def testIntersectionOut(x, y):
    res = -450 * x + 400 * y + 180000
    if ((res >= -550) and (res <= 550)):
        print (str(res))
        return True

    return False

camera = cv2.VideoCapture("test3.mp4")

firstFrame = None

while True:

    (grabbed, frame) = camera.read()


    if not grabbed:
        break

    frame = imutils.resize(frame, width=width)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue


    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 33, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)
    _, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        if cv2.contourArea(c) < 12000:
            continue


        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)




        rectagleCenterPont = ((x + x + w) /2, (y + y + h) /2)
        yuka_x = (x + x + w) /2
        yuka_y = (y + y + h) /2

        data = {"x": int(yuka_x),"y": int(yuka_y)}
        results = db.child("users").child("a").set(data, user['idToken'])

        #print (rectagleCenterPont, yuka_x, yuka_y)
        #cv2.circle(frame, rectagleCenterPont, 1, (0, 0, 255), 5)





    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    cv2.imshow("Security Feed", frame)


# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
