import requests
import random

def api_reddit(num:int = 50) -> dict:
    reddit_api_url = f'https://www.reddit.com/r/ProgrammerHumor/hot/.json?limit={num}';
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(reddit_api_url, headers=headers)

    if response.status_code != 200:
        result = {'status_code': response.status_code, 'reason': response.reason}
        return result
    
    response_data = response.json()
    rnd_num = random.randint(0,len(response_data['data']['children']))

    title = response_data['data']['children'][rnd_num]['data']['title']
    img_url = response_data['data']['children'][rnd_num]['data']['url']
    result = {'status_code': response.status_code, 'reason': response.reason, 'title': title, 'img_url': img_url}
       
    return result