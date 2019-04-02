import requests as req
import random as ra
#ONLY 6 PARKING SPOTS

empty = 'EMPTY'
occupied = 'OCCUPIED'

url = 'https://smartparking00.herokuapp.com'

def updateSpot(Spot,Status):
    r = req.post(url + '/api/' + 'update/' + str(Spot) + '/' + Status)
    d = r.text
    print(d)

def getJSON():
    r = req.get(url + '/api/getjson')
    d = r.json()
    print(d)


while True:
    if ra.randint(0,4) % 2 ==0:
     updateSpot(3,occupied)
    else:
     updateSpot(3,empty)
    if ra.randint(0,4) % 2 ==0:
     updateSpot(2,occupied)
    else:
     updateSpot(2,empty)
    if ra.randint(0,4) % 2 ==0:
     updateSpot(1,occupied)
    else:
     updateSpot(1,empty)
    if ra.randint(0,4) % 2 ==0:
     updateSpot(4,occupied)
    else:
     updateSpot(4,empty)
