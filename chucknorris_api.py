import requests
import random

def api_chucknorris(num:int = 50) -> dict:
    chucknorris_api_url = f'https://api.chucknorris.io/jokes/random';
    response = requests.get(chucknorris_api_url)

    if response.status_code != 200:
        result = {'status_code': response.status_code, 'reason': response.reason}
        return result

    response_data = response.json()
    result = {'status_code': response.status_code, 'reason': response.reason, 'value': response_data['value']}

    return result
