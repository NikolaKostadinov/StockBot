import datetime, pytz

def Now(): return datetime.datetime.now(tz=pytz.timezone("Europe/Sofia"))
def NowString(): return datetime.datetime.now(tz=pytz.timezone("Europe/Sofia")).strftime("%H:%M")