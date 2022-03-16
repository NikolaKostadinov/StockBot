import calendar as c

def ConvertDate(date):
    date = date.utctimetuple()
    return c.timegm(date)