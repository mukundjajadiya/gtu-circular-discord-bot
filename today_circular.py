import requests
from datetime import date, datetime
import pytz

UTC = pytz.utc
india_time = pytz.timezone('Asia/Kolkata')

date = datetime.now(india_time).strftime('%d-%b-%Y')

def get_today_circular():
    result = []
    URL = "https://gtu-api-2021.herokuapp.com/today-circular"
    today_circulars = requests.get(URL).json()

    for circular in today_circulars:
        try:
            if circular["date"]:
                result.append(circular)
        except:
            return circular["Note"]

    return result

def get_time():
    return datetime.now(india_time).strftime('%H:%M:%S')

