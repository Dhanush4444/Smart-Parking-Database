import requests as req

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


if __name__ == '__main__':
    updateSpot(5,occupied)
    updateSpot(1,empty)
    updateSpot(2,empty)
