import telebot


bot = telebot.TeleBot('5307565681:AAF2rQrwXKPOAWuXg_WQU6YhbWGE4q6-M6M')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(message)
def obligation_calculation():
    """Calculation"""
    if message.text == '/calc':
        bot.send_message(message)
bot.polling(none_stop=True)