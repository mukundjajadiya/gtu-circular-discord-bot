import requests
from datetime import date, datetime
import pytz

UTC = pytz.utc
india_time = pytz.timezone('Asia/Kolkata')

date = datetime.now(india_time).strftime('%d-%b-%Y')

def get_old_circular_list():
    result = []
    URL = 'https://gtu-api-2021.herokuapp.com/'
    response = requests.get(URL).json()

    for circular in response:
        # if circular['date'] != '25-Aug-2021':
        if circular['date'] != date:
            result.append(circular)

    return result

