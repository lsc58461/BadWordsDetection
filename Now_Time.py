import datetime

def Time():
    try:
        now = datetime.datetime.now()
        return now
    except:
        return "시간을 알 수 없습니다."