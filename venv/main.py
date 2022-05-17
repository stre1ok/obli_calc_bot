import telebot
from telebot import types


price, basePrice, bondCoupon, periodInAge = 0, 0, 0, 0

bot = telebot.TeleBot('5307565681:AAF2rQrwXKPOAWuXg_WQU6YhbWGE4q6-M6M')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Напиши /calc для расчета')

@bot.message_handler(func=lambda message: True)
def obligation_calculation(message):
    """Calculation"""
    if message.text == '/calc':
        bot.send_message(message.from_user.id, "Введите стоимость облигации в валюте(ПРИМЕР: Если 879.69руб, то 879.69)")
        bot.register_next_step_handler(message, what_price)

def what_price(message):
    global price
    price = float(message.text)
    bot.send_message(message.from_user.id, "Введите номинал облигации в валюте(ПРИМЕР: Если 1000руб, то 1000)")
    bot.register_next_step_handler(message, what_basePrice)

def what_basePrice(message):
    global basePrice
    basePrice = float(message.text)   
    bot.send_message(message.from_user.id, "Введите доходность купона облигации в процентах(ПРИМЕР: Если 7.5%, то 7.5)")
    bot.register_next_step_handler(message, what_bondCoupon)
    
def what_bondCoupon(message):
    global bondCoupon
    bondCoupon = float(message.text)
    bot.send_message(message.from_user.id, "Введите укажите количество до погашения облигации(ПРИМЕР: Если 2 года 6 месяцев, то 2.6)")
    bot.register_next_step_handler(message, what_periodInAge)
    
def what_periodInAge(message):
    global periodInAge
    periodInAge = float(message.text)
    s1 = f"Доходность от разницы номинала: {round((((price/basePrice*100)-100)*-1), 2)}%"
    s2 = f"Доходность от разницы номинала c учетом НДФЛ 13%: {round(((((price/basePrice*100)-100)*-1)*0.87), 2)}%"
    s3 = f"Доходность от разницы номинала в год: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))), 2)}%"
    s4 = f"Доходность от разницы номинала в год с учетом НДФЛ 13%: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))*0.87), 2)}%"
    s5 = f"Общая доходность в год: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+bondCoupon), 2)}%"
    s6 = f"Общая доходность в год с учетом НДФЛ 13%: {round(((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+bondCoupon)*0.87), 2)}%"
    bot.send_message(message.from_user.id, s1, s2, s3, s4, s5, s6)
    
    '''
    bot.send_message(message.from_user.id, f"Доходность от разницы номинала: {round((((price/basePrice*100)-100)*-1), 2)}%")
    bot.send_message(message.from_user.id, f"Доходность от разницы номинала c учетом НДФЛ 13%: {round(((((price/basePrice*100)-100)*-1)*0.87), 2)}%")
    bot.send_message(message.from_user.id, f"Доходность от разницы номинала в год: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))), 2)}%")
    bot.send_message(message.from_user.id, f"Доходность от разницы номинала в год с учетом НДФЛ 13%: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))*0.87), 2)}%")
    bot.send_message(message.from_user.id, f"Общая доходность в год: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+bondCoupon), 2)}%")
    bot.send_message(message.from_user.id, f"Общая доходность в год с учетом НДФЛ 13%: {round(((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+bondCoupon)*0.87), 2)}%")
    '''
    
bot.polling(none_stop=True)
