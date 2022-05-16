import telebot
from telebot import types


bot = telebot.TeleBot('5307565681:AAF2rQrwXKPOAWuXg_WQU6YhbWGE4q6-M6M')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(func=lambda message: True)
def obligation_calculation(message):
    """Calculation"""
    if message.text == '/calc':
        bot.send_message(message.chat.id, 'Введите стоимость облигации(в валюте)')
        price = message.text
        bot.send_message(message.chat.id, 'Введите номинал облигации(в валюте)')
        basePrice = message.text
    else:
        bot.reply_to(message, message.text)

bot.polling(none_stop=True)

"""
price = int(input("Введите стоимость облигации(в валюте):")) 
basePrice = int(input("Введите номинал облигации(в валюте):")) 
bondCoupon = float(input("Введите доходность купона облигации(в процентах):")) 
periodInAge = float(input("Введите укажите количество до погашения облигации(пример 2 года 6 месяцев = 2.6):"))
 
print("Доходность от разницы номинала=", ((price/basePrice*100)-100)*-1) 
print("Доходность от разницы номинала c учетом НДФЛ 13%=", (((price/basePrice*100)-100)*-1)*0.87) 
print("Доходность от разницы номинала в год=",((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))) 
print("Доходность от разницы номинала в год с учетом НДФЛ 13%=",((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))*0.87) 
print("Общая доходность в год=",((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+bondCoupon) 
print("Общая доходность в год с учетом НДФЛ 13%=",(((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+bondCoupon)*0.87)
"""
