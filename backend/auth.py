
import json,uuid,os

FILE="config/users.json"

def load():
    if not os.path.exists(FILE):
        return {"current":None,"accounts":[]}
    return json.load(open(FILE))

def save(d):
    json.dump(d,open(FILE,"w"))

def login(qq):
    d=load()
    t=str(uuid.uuid4())
    user={"id":qq,"token":t}
    d["current"]=user
    d["accounts"].append(user)
    save(d)
    return user
