import requests
import json
from clock import clock

def schedule(idGroup):
	sch = [[] for i in range(7)]

	times = clock()
	url = 'http://oreluniver.ru/schedule//{}///{}/printschedule'.format(idGroup, str(times) + '000')

	r = json.loads(requests.get(url).text)
	r = sorted(r, key=lambda item: item['DayWeek'])

	for i in range(len(r)):
		if (i == 0) or (r[i]['NumberLesson'] != r[i-1]['NumberLesson']):
			sch[r[i]['DayWeek'] - 1].append( 
				'{0}. {1} ({2}).\nАудитория: {3}'.format(str(r[i]['NumberLesson']),
														r[i]['TitleSubject'], r[i]['TypeLesson'],
														r[i]['Korpus'] + '-' + r[i]['NumberRoom'])
			)


	for i in range(7):
		if not sch[i]:
			sch[i] = ['Пар нет'] 

	return sch

