USE_TG = True
USE_QMSG = True
TG_BOT_TOKEN = ''
TG_USER_ID = ''
TG_API_HOST = 'api.telegram.org'
QMSG_HOST = 'qmsg.zendee.cn/'
QMSG_API_KEY = ''
QMSG_USER_ID = ''
headers = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RD2A.211001.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.120 Mobile Safari/537.36 MMWEBID/977 MicroMessenger/8.0.16.2040(0x28001037) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/en ABI/arm64',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'openId=xxxx; JSESSIONID=xxx'
}
data='openId=xxxx&userXq=xxxx&userFj=xxxx'
url = 'http://www.stuzf.sdu.edu.cn/wxapp/api/pay/queryElectricity'
