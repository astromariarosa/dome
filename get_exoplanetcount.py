import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# inputs after calling script
# default to all confirmed


url = 'https://exoplanetarchive.ipac.caltech.edu/index.html'

response = requests.get(url)

# check if it's working:
if str(response) == '<Response [200]>':
    print('Access Successful!')
    soup = BeautifulSoup(response.text, "html.parser")

    #soup.findAll('a')
    # trial and error to find the right line:
    conf = soup.find_all('a')[77]
    conf_t = [t for t in conf.stripped_strings]
    conf_count = conf_t[0]
    conf_desc = conf_t[1]
    conf_date = conf_t[2]

    # TESS confirmed
    tess = soup.find_all('a')[78]
    tess_t = [t for t in tess.stripped_strings]
    tess_count = tess_t[0]
    tess_desc = tess_t[1]
    tess_date = tess_t[2]

    # TESS candidates
    tesscan = soup.find_all('a')[79]
    tesscan_t = [t for t in tesscan.stripped_strings]
    tesscan_count = tesscan_t[0]
    tesscan_desc = tesscan_t[1]
    tesscan_date = tesscan_t[2]

    print('\n'+conf_count, conf_desc)
    print('Updated', conf_date)

    print('\n'+tess_count, tess_desc)
    print('Updated', tess_date)

    print('\n'+tesscan_count, tesscan_desc)
    print('Updated', tesscan_date)

else:
    print('Access Unsuccessful. Script Aborted.')
