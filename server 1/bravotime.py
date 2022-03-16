import datetime, pytz

def Now():
    
    """Return date in bravo time zone as datetime"""
    
    return datetime.datetime.now(tz=pytz.timezone("Europe/Sofia"))

def NowString():
    
    """Return date in bravo time zone as a string"""
    
    return Now().strftime("%H:%M")

def Convert(date):
    
    """Convert any date to bravo time zone datetime"""
    
    return date.astimezone(tz=pytz.timezone("Europe/Sofia"))