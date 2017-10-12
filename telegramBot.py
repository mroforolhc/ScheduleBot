# TRUE EXCEPT ДЛЯ ЗАПИСИ В БД ПОШАГОВЫХ ДАННЫХ

import requests
import json
import telebot
from telebot import types

import time
import datetime

from settings import token, db_url
from data import idGroups, idFaculties, weekDays, schCalls
from clock import clock
from dbTools import UserPosition
from schedule import schedule
from simpleKeyboard import Keyboard


bot = telebot.TeleBot(token)
keyboard = Keyboard(bot)
up = UserPosition(db_url)


@bot.message_handler(commands=['start'])
def handle_start(message):
	keyboard.getMainMenu(message)

@bot.message_handler(func=lambda message: 'Главное меню' == message.text, content_types=['text'])
def handle_start(message):
	up.cancel_getting_started(str(message.chat.id))
	keyboard.getMainMenu(message)

@bot.message_handler(func=lambda message: 'Расписание звонков' == message.text, content_types=['text'])
def handle_start(message):
	bot.send_message(message.from_user.id, schCalls)

@bot.message_handler(func=lambda message: 'Обратная связь' == message.text, content_types=['text'])
def handle_start(message):
	bot.send_message(message.from_user.id, 'Все баги и пожелания сюда: @markov_ka')

@bot.message_handler(func=lambda message: 'Получить расписание' == message.text, content_types=['text'])
def option(message):
	up.set_getting_position(str(message.chat.id))
	keyboard.getFaculties(message)

# Перехват факультетов
@bot.message_handler(func=lambda message: message.text in list(idFaculties), content_types=['text'])
def option(message):
	up.set_faculty_position(str(message.chat.id), message.text)
	idF, idC = up.get_faculty_and_course(str(message.chat.id))
	id = idFaculties[idF]
	keyboard.getCourses(message, id)

# Перехват курса	
@bot.message_handler(func=lambda message: message.text in ['1', '2', '3', '4', '5', '6'], content_types=['text'])
def option(message):
	try:
		up.set_course_position(str(message.chat.id), message.text)
		idF, idC = up.get_faculty_and_course(str(message.chat.id))
		keyboard.getGroups(message, idF, idC)
	except:
		pass

# Перехват группы
@bot.message_handler(func=lambda message: message.text in list(idGroups), content_types=['text'])
def option(message):
	try:
		up.set_group_position(str(message.chat.id), message.text)
		keyboard.getSchedule(message)
	except:
		pass
		
@bot.message_handler(func=lambda message: 'На сегодня' == message.text or 
											'На завтра' == message.text, content_types=['text'])
def option(message):
	idG = up.verification(str(message.chat.id)) # получение группы из БД
	sch = schedule(idGroups[idG])               # парс расписания
	now_date = datetime.date.today()      
	weekDay = now_date.weekday()           
	dt = time.time()                            
	send = ''

	if message.text == 'На завтра':
		weekDay += 1
		dt += 86400         # +1 день времени в секундах
		if weekDay == 7:
			weekDay = 0

	send += '{} - {}:\n\n'.format(time.strftime('%d.%m.%Y', time.localtime(dt)), weekDays[weekDay])
	for i in sch[weekDay]:
		send = send + i + '\n'
	bot.send_message(message.from_user.id, send)

@bot.message_handler(func=lambda message: 'На неделю' == message.text, content_types=['text'])
def option(message):
	idG = up.verification(str(message.chat.id)) # получение группы из БД
	sch = schedule(idGroups[idG])               # парс расписания  
	dateMon = time.strftime('%d.%m.%Y', time.localtime(clock() + 86400))
	dateSat = time.strftime('%d.%m.%Y', time.localtime(clock() + 86400*6))
	send = '{} - {}\n\n'.format(dateMon, dateSat)

	for day in range(len(sch)-1):
		send += weekDays[day] + ':\n'
		for i in sch[day]:
			send += i + '\n'
		send += '\n'
	bot.send_message(message.from_user.id, send)



@bot.message_handler(func=lambda message: 'Вернуться назад' == message.text, content_types=['text'])
def option(message):
	key = up.back_keyboard(str(message.chat.id))
	if key == 1:
		up.cancel_getting_started(str(message.chat.id))
		keyboard.getMainMenu(message)
	elif key == 2:
		up.cancel_faculty(str(message.chat.id))
		keyboard.getFaculties(message)
	elif key == 3:
		up.cancel_course(str(message.chat.id))
		idF, idC = up.get_faculty_and_course(str(message.chat.id))
		id = idFaculties[idF]
		keyboard.getCourses(message, id)
	elif key == 4:
		up.cancel_group(str(message.chat.id))
		idF, idC = up.get_faculty_and_course(str(message.chat.id)) 
		keyboard.getGroups(message, idF, idC)


if __name__ == "__main__":
	while True:
		try:
			bot.polling(none_stop = True)
		except Exception as e:
			print(e)
			time.sleep(5)
