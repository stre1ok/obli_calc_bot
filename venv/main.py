import telebot


bot = telebot.Telebot('5307565681:AAF2rQrwXKPOAWuXG_WQU6YhbWGE4q6-M6M')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message()
