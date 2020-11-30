import telebot
import cfg
from telebot import types

bot = telebot.TeleBot(cfg.token)


@bot.message_handler(commands=['start'])
def start_message(message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton(text='Регистрация', callback_data='reg'))
	markup.add(types.InlineKeyboardButton(text='Как работает бот?', callback_data='how'))
	markup.add(types.InlineKeyboardButton(text='Начать подбор машины', callback_data='car'))
	bot.send_message(message.chat.id, text='Доброго времени суток. \b Позвольте представиться, я Drug. \b Подбодбираю машины любых марок и расценок, вам нужно лишь пройти небольшую регистрацию прямо здесь и указать критерии подбора машин для меня. \b Ну что, приступим!'
    	, reply_markup=markup)


@bot.message_handler(commands=['reg'])
def start_registretion(message):
	


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

	bot.answer_callback_query(callback_query_id=call.id, text='Хороший выбор!')
	answer = ''
	if call.data == 'reg':
		answer = 'Окей, приступим.'
		bot.send_message(call.message.chat.id, answer)
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
	elif call.data == 'how':
		answer = 'Смотри'
		bot.send_message(call.message.chat.id, answer)
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
	elif call.data == 'car':
		answer = 'Поехали.'
		bot.send_message(call.message.chat.id, answer)
		bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)



bot.polling(none_stop=True)