import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# get current time in utc
now = datetime.now(pytz.utc)

# url where xml file for RVA is located
url = 'https://spotthestation.nasa.gov/sightings/xml_files/United_States_Virginia_Richmond.xml'

response = requests.get(url)

# check if it's working:
if str(response) == '<Response [200]>':
    print('Access Successful!')
    soup = BeautifulSoup(response.text, "html.parser")

    iss = soup.find_all('item')

    sightings = len(iss)

    for index, item in enumerate(iss):
        txt = [t for t in iss[index].stripped_strings]

        # date and time for the ISS sighting:
        info = txt[2]  # gives all the info together
        split = info.split()

        find_date = split.index('Date:')
        d = split[find_date+2:find_date+5] # ['Mar', '9,', '2021']
        find_time = split.index('Time:')
        t = split[find_time+1:find_time+3] # ['6:12', 'AM'] so this is EST

        # load it as a datetime object with some creative formatting
        dt = datetime.strptime(d[0]+' '+d[1]+' '+d[2]+' '+t[0]+t[1], '%b %d, %Y %I:%M%p')
        # localize it to utc in one line:
        dt_tz = pytz.timezone('est').localize(dt)

        # we don't care about sightings that have already passed
        if dt_tz < now:
            sightings = sightings - 1
            pass
        else:
            print(info)
    print(sightings, 'Total ISS Sightings Listed')
else:
    print('Access Unsuccessful. Script Aborted.')
