from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def GetCandleStickInformations(symbol, interval, startTime,	endTime):
    url = 'https://api.binance.com/api/v3/klines'
    parameters = {
        'symbol': symbol,
        'interval': interval,
        'startTime': startTime,
        'endTime': endTime
    }

    headers = {
        'Accepts': 'application/json',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        return "Error"