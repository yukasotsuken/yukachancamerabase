import pyrebase
import sys
import datetime
import time
import json
import dataTransfer



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




def enviar(nk,id,x,y,tm):
    data = {"nk": nk, "id": id,"x": int(x),"y": int(y), "time": tm}
    results = db.child("floor3").child(id).set(data, user['idToken'])


def getData(data):
        for u in data:
            enviar(u['nk'],u['id'],u['x'],u['y'],u['tm'])


def readFile():
    with open('data.json') as json_file:
        data = json.load(json_file)
        getData(data)
