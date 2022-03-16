import datetime as t
import calendar as c

current_datetime = t.datetime(2020, 5, 19)
current_timetuple = current_datetime.utctimetuple()
current_timestamp = c.timegm(current_timetuple)

print(current_timestamp)