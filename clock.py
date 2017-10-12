import time

def clock():
	times = int(time.time())

	day = int(time.strftime('%w', time.localtime(times))) * 60 * 60 * 24 
	hour = int(time.strftime('%H', time.localtime(times))) * 60 * 60
	min = int(time.strftime('%M', time.localtime(times))) * 60
	sec = int(time.strftime('%S', time.localtime(times)))
	all = day + hour + min + sec

	now = (times - all + (3600 * 3)) # округление до 00:00 
	
	return now
