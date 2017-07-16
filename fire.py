import pyrebase
import sys
import datetime
import time
import json
import delData



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



def say(id):
    print("borrar " + str(id))
    with open('data.json', 'r+') as f:
        json_data = json.load(f)
        for i in json_data:
            if i['id'] == id:
                json_data.remove(i)
        f.seek(0)
        f.write(json.dumps(json_data))
        f.truncate()



def enviar(nk,id,x,y,tm,destroy):
    data = {"nk": nk, "id": id,"x": int(x),"y": int(y), "time": tm}
    if(destroy == False):
        results = db.child("floor3").child(id).set(data, user['idToken'])
    else:
        db.child("floor3").child(id).remove(user['idToken'])
        say(id)







def getData(data):
        if len(data) > 0:
            for u in data:
                if(time.time()-u['tm']>5):
                    enviar(u['nk'],u['id'],u['x'],u['y'],u['tm'], True)
                else:
                    enviar(u['nk'],u['id'],u['x'],u['y'],u['tm'], False)




def readFile():
    with open('data.json') as json_file:
        data = json.load(json_file)
        getData(data)
