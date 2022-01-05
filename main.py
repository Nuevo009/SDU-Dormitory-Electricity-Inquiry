from config import *
from utils import *

def main():
    tg = Telegram(TG_API_HOST, TG_BOT_TOKEN, TG_USER_ID)
    qmsg = Qmsg(QMSG_HOST, QMSG_API_KEY, QMSG_USER_ID)
    Msg = GetMsg(url, headers, data)
    if USE_TG:
        tg.send_message(Msg)
    if USE_QMSG:
        qmsg.send_message(Msg)
if __name__ == "__main__":
    main()