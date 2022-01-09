import time
import requests
from config import *
class Telegram:
    def __init__(self, host, token, user_id):
        self.host = host
        self.token = token
        self.user_id = user_id

    def send_message(self, text):
        data = (('chat_id', self.user_id), ('text', text))
        response = requests.post(url=f"https://{self.host}/bot{self.token}/sendMessage",
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
        response = requests.post(url=f"https://{self.host}/send/{self.api_key}", data=data)
        if response.status_code != 200:
            print('Qmsg 推送失败，原因可能为网络问题，err_code:', response.status_code)
        elif response.json()['code'] != 0:
            print(f'Qmsg 推送失败，具体原因为：{response.json()["reason"]}')
        else: print('Qmsg 推送成功')

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
            time.sleep(sleep_seconds)
        else:
            return response
def GetMsg(url, headers, data):
    response = request('POST', url, headers=headers, data=data).json()
    status = response['message']['status']
    elec = response['message']['plusElec']
    if status == '获取数据异常':
        return status
    elif float(elec) < 10.0:
        return f'您的电量不足 10 度，当前电量为 {elec}，请及时充电！'
    else: return f'您的电量为 {elec} 度，请放心使用！'
