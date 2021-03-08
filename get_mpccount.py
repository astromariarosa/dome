import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datetime import datetime

m = datetime.now().strftime('%B')
y = datetime.now().strftime('%Y')

# inputs after calling script
# default to all confirmed


url = 'https://minorplanetcenter.net/'

response = requests.get(url)

# check if it's working:
if str(response) == '<Response [200]>':
    print('Access Successful!')
    soup = BeautifulSoup(response.text, "html.parser")

    mpc = soup.find_all('aside')[0]

    # create a list of all the stripped string, should be length = 30
    mpc_t = [t for t in mpc.stripped_strings]

    neo_desc = mpc_t[1]

    neo_month_tally = mpc_t[3]
    neo_year_tally = mpc_t[5]
    neo_all_tally = mpc_t[7]

    mp_desc = mpc_t[8]

    mp_month_tally = mpc_t[10]
    mp_year_tally = mpc_t[12]
    mp_all_tally = mpc_t[14]

    com_desc = mpc_t[15]

    com_month_tally = mpc_t[17]
    com_year_tally = mpc_t[19]
    com_all_tally = mpc_t[21]

    obs_desc = mpc_t[22]

    obs_month_tally = mpc_t[24]
    obs_year_tally = mpc_t[26]
    obs_all_tally = mpc_t[28]

    print(neo_desc[:-11]+':')
    print(neo_month_tally, neo_desc[-10:], 'in', m, y)
    print(neo_year_tally, neo_desc[-10:], 'in', y)
    print(neo_all_tally, neo_desc[-10:], 'Total')

    print(mp_desc[:-11]+':')
    print(mp_month_tally, mp_desc[-10:], 'in', m, y)
    print(mp_year_tally, mp_desc[-10:], 'in', y)
    print(mp_all_tally, mp_desc[-10:], 'Total')

    print(com_desc[:-11]+':')
    print(com_month_tally, com_desc[-10:], 'in', m, y)
    print(com_year_tally, com_desc[-10:], 'in', y)
    print(com_all_tally, com_desc[-10:], 'Total')


else:
    print('Access Unsuccessful. Script Aborted.')
