import json
from fire import enviar

#create data
data = {}
#add users
data['users'] = []



def addData(id,nk,time,x,y):
    #append user
    data['users'].insert(id,{
        'id':id,
        'nk':nk,
        'time':time,
        'x': x,
        'y': y
    })


def writeFile():
    with open('data.json', 'r+') as f:
        json_data = json.load(f)
        json_data['users'] = data['users']
        f.seek(0)
        f.write(json.dumps(json_data))
        f.truncate()
