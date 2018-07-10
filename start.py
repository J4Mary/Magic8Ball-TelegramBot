from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from random import randint

updater = Updater('TOKEN')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# English
def help_en(bot, update):
	message = update.message
	answer = "Send me a message and I'll give you advice."
	
	bot.send_message(message.chat_id, answer)
	print(message.from_user.full_name + ': ' + message.text + ' | ' + 'Bot: ' + answer);

def echo_en(bot, update):
	message = update.message
	chat_id = message.chat_id
	answer = ''

	if message.text.lower().find('eric') > -1 or message.text.lower().find('erik') > -1 or message.text.lower().find('эрик') > -1:
		answer = 'He who must not be named...'
	else:
		value = randint(0, 19)

		if value == 0:
			answer = 'It is certain'
		elif value == 1:
			answer = 'It is decidedly so'
		elif value == 2:
			answer = 'Without a doubt'
		elif value == 3:
			answer = 'Yes — definitely'
		elif value == 4:
			answer = 'You may rely on it'
		elif value == 5:
			answer = 'As I see it, yes'
		elif value == 6:
			answer = 'Most likely'
		elif value == 7:
			answer = 'Outlook good'
		elif value == 8:
			answer = 'Signs point to yes'
		elif value == 9:
			answer = 'Yes'
		elif value == 10:
			answer = 'Reply hazy, try again'
		elif value == 11:
			answer = 'Ask again later'
		elif value == 12:
			answer = 'Better not tell you now'
		elif value == 13:
			answer = 'Cannot predict now'
		elif value == 14:
			answer = 'Concentrate and ask again'
		elif value == 15:
			answer = 'Don’t count on it'
		elif value == 16:
			answer = 'My reply is no'
		elif value == 17:
			answer = 'My sources say no'
		elif value == 18:
			answer = 'Outlook not so good'
		else:
			answer = 'Very doubtful'

	bot.send_message(chat_id, answer)
	print(message.from_user.full_name + ': ' + message.text + ' | ' + 'Bot: ' + answer);

def unknown_en(bot, update):
	message = update.message
	answer = "Sorry, I didn't understand that command."

	bot.send_message(message.chat_id, answer)
	print(message.from_user.full_name + ': ' + message.text + ' | ' + 'Bot: ' + answer);

start_en_handler = CommandHandler('start', help_en, filters = ~ Filters.language('ru'))
dispatcher.add_handler(start_en_handler)

help_en_handler = CommandHandler('help', help_en, filters = ~ Filters.language('ru'))
dispatcher.add_handler(help_en_handler)

echo_en_handler = MessageHandler(Filters.text & (~ Filters.language('ru')), echo_en)
dispatcher.add_handler(echo_en_handler)

unknown_en_handler = MessageHandler(Filters.command & (~ Filters.language('ru')), unknown_en)
dispatcher.add_handler(unknown_en_handler)

# Russian
def help_ru(bot, update):
	message = update.message
	answer = 'Отправь мне сообщение, и я дам тебе совет.'

	bot.send_message(message.chat_id, answer)
	print(message.from_user.full_name + ': ' + message.text + ' | ' + 'Bot: ' + answer);

def echo_ru(bot, update):
	message = update.message
	chat_id = message.chat_id
	answer = ''

	if message.text.lower().find('уверен') > -1:
		value = randint(0, 1)

		if value == 0:
			answer = 'Я уверен в этом.'
		else:
			answer = 'Я не уверен в этом.'
	elif message.text.lower().find('эрик') > -1 or message.text.lower().find('eric') > -1 or message.text.lower().find('erik') > -1:
		answer = 'Это тот, чьё имя нельзя называть...'
	else:
		value = randint(0, 19)

		if value == 0:
			answer = 'Бесспорно'
		elif value == 1:
			answer = 'Предрешено'
		elif value == 2:
			answer = 'Никаких сомнений'
		elif value == 3:
			answer = 'Определённо да'
		elif value == 4:
			answer = 'Можешь быть уверен в этом'
		elif value == 5:
			answer = 'Мне кажется — «да»'
		elif value == 6:
			answer = 'Вероятнее всего'
		elif value == 7:
			answer = 'Хорошие перспективы'
		elif value == 8:
			answer = 'Знаки говорят — «да»'
		elif value == 9:
			answer = 'Да'
		elif value == 10:
			answer = 'Пока не ясно, попробуй снова'
		elif value == 11:
			answer = 'Спроси позже'
		elif value == 12:
			answer = 'Лучше не рассказывать'
		elif value == 13:
			answer = 'Сейчас нельзя предсказать'
		elif value == 14:
			answer = 'Сконцентрируйся и спроси опять'
		elif value == 15:
			answer = 'Даже не думай'
		elif value == 16:
			answer = 'Мой ответ — «нет»'
		elif value == 17:
			answer = 'По моим данным — «нет»'
		elif value == 18:
			answer = 'Перспективы не очень хорошие'
		else:
			answer = 'Весьма сомнительно'

	bot.send_message(chat_id, answer)
	print(message.from_user.full_name + ': ' + message.text + ' | ' + 'Bot: ' + answer);

def unknown_ru(bot, update):
	message = update.message
	answer = 'Извините, я не понял эту команду.'

	bot.send_message(message.chat_id, answer)
	print(message.from_user.full_name + ': ' + message.text + ' | ' + 'Bot: ' + answer);

start_ru_handler = CommandHandler('start', help_ru, filters = Filters.language('ru'))
dispatcher.add_handler(start_ru_handler)

help_ru_handler = CommandHandler('help', help_ru, filters = Filters.language('ru'))
dispatcher.add_handler(help_ru_handler)

echo_ru_handler = MessageHandler(Filters.text & Filters.language('ru'), echo_ru)
dispatcher.add_handler(echo_ru_handler)

unknown_ru_handler = MessageHandler(Filters.command & Filters.language('ru'), unknown_ru)
dispatcher.add_handler(unknown_ru_handler)

updater.start_polling()