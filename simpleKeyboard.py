import telebot
from telebot import types
import json
import requests
from data import idFaculties

class Keyboard:
    def __init__(self, bot):
        self.bot = bot

    def getMainMenu(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Получить расписание')
        markup.row('Расписание по подписке (неактив)')
        markup.row('Расписание звонков')
        markup.row('Обратная связь')
        self.bot.send_message(message.chat.id, 'Выберите пункт меню:', reply_markup=markup)

    def getFaculties(self, message):
        markup = telebot.types.ReplyKeyboardMarkup()
        markup.row('Вернуться назад')
        markup.row('ИПАИТ')
        markup.row('ИВЗО', 'ЮИ', 'АСИ')
        markup.row('ИБиБ', 'ФКС', 'ФЕН')
        markup.row('ИЭиУ', 'ПТИ', 'ХГФ')
        self.bot.send_message(message.from_user.id, 'Выберите факультет:', reply_markup=markup)

    def getCourses(self, message, id):
        url = 'http://oreluniver.ru/schedule/{}/kurslist'.format(id)
        r = json.loads(requests.get(url).text)
        
        courses = []
        for _ in r:
            courses.append(str(_['kurs']))
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Вернуться назад')
        markup.add(*[types.KeyboardButton(name) for name in courses])
        self.bot.send_message(message.from_user.id, 'Выберите курс:', reply_markup=markup)

    def getGroups(self, message, idF, idC):  
        url = 'http://oreluniver.ru/schedule/{}/{}/grouplist'.format(idFaculties[idF], idC)
        r = json.loads(requests.get(url).text)
        groups = []
        for _ in r:
            groups.append(str(_['title']))
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('Вернуться назад')
        markup.add(*[types.KeyboardButton(name) for name in groups])
        self.bot.send_message(message.from_user.id, 'Выберите группу:', reply_markup=markup)

    def getSchedule(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('На сегодня', 'На завтра')
        markup.row('На неделю')
        markup.row('Подписаться на группу (неактив)')
        markup.row('Главное меню', 'Вернуться назад')
        self.bot.send_message(message.from_user.id, 'Выберите дату:', reply_markup=markup)
