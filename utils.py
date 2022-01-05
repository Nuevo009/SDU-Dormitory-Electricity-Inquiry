import time
import logging
import requests
from config import *
class Telegram:
    def __init__(self, host, token, user_id):
        self.host = host
        self.token = token
        self.user_id = user_id

    def send_message(self, text):
        data = (('chat_id', self.user_id), ('text', text))
        response = requests.post(f"https://{TG_API_HOST}/bot{self.token}/sendMessage",
                                 data=data)
        if response.status_code != 200:
            print('Telegram Bot 推送失败')
        else:
            print('Telegram Bot 推送成功')
class Qmsg:
    def __init__(self, host, api_key, user_id):
        self.host = host
        self.api_key = api_key
        self.user_id = user_id

    def send_message(self, text):
        data = (('qq', self.user_id),
                ('msg', text))
        response = requests.post(f"https://{self.host}/send/{self.api_key}", data=data)
        if response.status_code != 200:
            print('Qmsg 推送失败')
        else:
            print('Qmsg 推送成功')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
log = logger = logging
def request(*args, **kwargs):
    is_retry = True
    count = 0
    max_retries = 3
    sleep_seconds = 5
    while is_retry and count <= max_retries:
        try:
            s = requests.Session()
            response = s.request(*args, **kwargs)
            is_retry = False
        except Exception as e:
            if count == max_retries:
                raise e
            log.error(f'Request failed: {e}')
            count += 1
            log.info(
                f'Trying to reconnect in {sleep_seconds} seconds ({count}/{max_retries})...')
            time.sleep(sleep_seconds)
        else:
            return response
def GetMsg(url, headers, data):
    status =  request('POST', url, headers=headers, data=data).json()
    return f"⚡剩余电量⚡ \n\n{status['message']['plusElec']} 度"
