import random
from datetime import datetime, timedelta

def gen_datetime(min_vuosi=2019, max_vuosi=datetime.now().year):
    '''
    luo satunnainen datetime() päivämäärä annetulla välillä.
    muodossa yyyy-mm-dd hh:mm:ss.000000
    '''
    # generate a datetime in format yyyy-mm-dd hh:mm:ss.000000
    alku = datetime(min_vuosi, 1, 1, 00, 00, 00)
    vuosia = max_vuosi - min_vuosi + 1
    loppu = alku + timedelta(days=365 * vuosia)
    return alku + (loppu - alku) * random.random()