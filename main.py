from config import *
from utils import *

def main():
    tg = Telegram(TG_API_HOST, TG_BOT_TOKEN, TG_USER_ID)
    qmsg = Qmsg(QMSG_HOST, QMSG_API_KEY, QMSG_USER_ID)
    msg = GetMsg(url, headers, data)
    if USE_TG:
        tg.send_message(msg)
    if USE_QMSG:
        qmsg.send_message(msg)
if __name__ == "__main__":
    main()