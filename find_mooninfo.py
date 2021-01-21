# This script gives you information about the moon in one quick line.

# To execute, type into the Command line:
# python find_mooninfo.py

# Mariarosa Marinelli
# mmarinelli@smv.org

import pylunar
from datetime import datetime
import pytz

# get current datetime, which will be naive
now = datetime.now()

# make the datetime aware of the local timezone
eastern = pytz.timezone('US/Eastern')
now = eastern.localize(now)
now_str = now.strftime("%Y-%m-%d %H:%M:%S")

# convert to UTC for the pylunar module
utc = pytz.timezone('UTC')
now_utc = now.astimezone(utc)

def get_moon_info(x):
    if isinstance(x, datetime) == True:
        # convert datetime to string
        x_str = x.strftime("%Y-%m-%d %H:%M:%S")

        # slice string to use in pylunar function
        year = int(x_str[0:4])
        mes = int(x_str[5:7])
        day = int(x_str[8:10])
        hr = int(x_str[11:13])
        min = int(x_str[14:16])
        sec = int(x_str[17:19])

        # call pylunar MoonInfo function with correct coordinates
        moon = pylunar.MoonInfo((37, 32, 10.82), (-77, 27, 24.85))
        # use the current date in UTC format
        moon.update((year, mes, day, hr, min, sec))

        # moon phase:
        print(moon.phase_name())
        fp_now = moon.fractional_phase()
        print('{:.1%}'.format(fp_now)+' full')

        # age since last new moon
        age = moon.age()
        print('{:.2}'.format(age)+' days since last New Moon')

        # get the local rising and setting times
        rise_set = moon.rise_set_times('US/Eastern') # list

        # have to slice through list
        for i in range(3):
            if 'rise' in rise_set[i]:
                rise = rise_set[i]
                rise_time = rise[1]  #0th in list is the label

                # create datetime, will be naive
                rise_dt = datetime(rise_time[0], rise_time[1],
                                   rise_time[2], rise_time[3],
                                   rise_time[4], rise_time[5])

                # make datetime aware of local time zone
                rise_dt = eastern.localize(rise_dt)
                rise_dt_str = rise_dt.strftime("%Y-%m-%d %H:%M:%S")

                # compare rising time to current time
                if rise_dt > now:
                    print('The Moon will rise today at: '+ rise_dt_str)
                elif rise_dt < now:
                    print('The Moon rose today at: '+ rise_dt_str)
                else:
                    print('It seems that the Moon is rising right now!')

            elif 'set' in rise_set[i]:
                set = rise_set[i]
                set_time = set[1]  #0th in list is the label

                # create datetime, will be naive
                set_dt = datetime(set_time[0], set_time[1],
                                  set_time[2], set_time[3],
                                  set_time[4], set_time[5])

                # make datetime aware of local time zone
                set_dt = eastern.localize(set_dt)
                set_dt_str = set_dt.strftime("%Y-%m-%d %H:%M:%S")

                # compare setting time to current time
                if set_dt > now:
                    print('The Moon will set today at: '+ set_dt_str)
                elif set_dt < now:
                    print('The Moon set today at: '+ set_dt_str)
                else:
                    print('It seems that the Moon is setting right now!')

            # we don't care about the transit times
            elif 'transit' in rise_set[i]:
                pass

    else:
        print('Something has gone wrong with the datetime verification!')

get_moon_info(now_utc)
