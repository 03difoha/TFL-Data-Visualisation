import settings
import urllib2
import json
import datetime

tfl_key = 'XXXXXXXX'
tfl_id = 'XXXXXXXX'

tfl_url = "XXXXXXXXX"
tfl_json = urllib2.urlopen(tfl_url)
tfl_data = json.load(tfl_json)
d = datetime.datetime.now()
hours = str(int(d.hour))
day = str(d.strftime("%A"))
theTime = str(d.strftime("%H:%M"))


def recAv():
    #user = auth.refresh(user['refreshToken'])
    for item in tfl_data:
        bays = item['bays']
        for i in bays:
            free = {theTime: i['free']}
            settings.db.child("Car Parks").child(item['name']).child(i['bayType']).child(day).child(hours)\
            .update(free, settings.user['idToken'])

recAv()

