import requests

from fastapi import FastAPI


import schemas

app = FastAPI()

#fixar en databas
minDatabase = {
    1:{'task':'mun och tander'},
    2:{'task':'forkylning och vark'},
    3:{'task':'kroppsvard'},
}


@app.get("/")
def getItems():
    return minDatabase

@app.get("/{id}")
def getItem(id:int):
    return minDatabase[id]

#fall 1
#@app.post("/")   
#def addItem(task:str):
#   newId = len(minDatabase.keys()) + 1 #fixat ny id och rakna hur manga keys har vi i mitt fatt har jag 3 st,+1 lagg till nya varde
    #minDatabase[newId] = {"task":task}
    #return minDatabase






#fall 2

@app.post("/")   
def addItem(item:schemas.Item):
    newId = len(minDatabase.keys()) + 1 #fixat ny id och rakna hur manga keys har vi i mitt fatt har jag 3 st,+1 lagg till nya varde
    minDatabase[newId] = {"task":item.task}
    return minDatabase


@app.put("/{id}")
def updateItem(id:int, item:schemas.Item):
    minDatabase[id]['task'] = item.task
    return minDatabase


@app.delete("/{id}")
def deleteItem(id:int):
    del minDatabase[id] # detta innebar att jag ska deleta den id parameter fran min databas
    return minDatabase


