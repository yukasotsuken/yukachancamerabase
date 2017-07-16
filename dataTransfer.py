import json
import time
import subprocess
import threading
import run

datos = []


def putData (id,nk,tm,x,y):
    user = {'id':id, 'nk': nk, 'tm': tm, 'x': x, 'y': y}
    if len(datos)>0 and id-1 < len(datos):
        del datos[id-1]
    datos.insert(id-1, user)








def writeFile():
    #print(len(datos))
    with open('data.json', 'r+') as f:
        json_data = json.load(f)
        json_data = datos
        f.seek(0)
        f.write(json.dumps(json_data))
        f.truncate()
    #subprocess.call('python3 fire.py', shell=True)
