import telebot
from telebot import types


price, basePrice, bondCoupon, periodInAge = 0, 0, 0, 0

bot = telebot.TeleBot('5307565681:AAF2rQrwXKPOAWuXg_WQU6YhbWGE4q6-M6M')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Напиши /calc для расчёта облигации\nНапиши /ccalc для расчёта ящика')

@bot.message_handler(func=lambda message: True)
def obligation_calculation(message):
    if message.text == '/calc':
        bot.send_message(message.from_user.id, "Введите стоимость облигации в валюте(ПРИМЕР: Если 879.69руб, то 879.69)")
        bot.register_next_step_handler(message, what_price)
    if message.text == '/ccalc':
        bot.send_message(message.from_user.id, "Введите стоимость ящика")
        bot.register_next_step_handler(message, what_crate_price)

'''*******************Рассчёт ящика*******************'''
def what_crate_price(message):
    crate_price = message.text
    while type(crate_price) != float:
        try:
            crate_price = float(crate_price)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводи цифрами.')
            break

    if type(crate_price) != float or crate_price <= 0:
        bot.send_message(message.from_user.id, "Введите стоимость ящика")
        bot.register_next_step_handler(message, what_crate_price)
    else:
        bot.send_message(message.from_user.id, f"Цена продажи ящика в 0: {round(crate_price/0.85), 2}")
        crate_price = 0

'''*******************Рассчёт облигации*******************'''
def what_price(message):
    global price
    price = message.text
    while type(price) != float:
        try:
            price = float(price)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводи цифрами.')
            break

    if type(price) != float or price <= 0:
        bot.send_message(message.from_user.id, "Введите стоимость облигации в валюте(ПРИМЕР: Если 879.69руб, то 879.69)")
        bot.register_next_step_handler(message, what_price)
    else:
        bot.send_message(message.from_user.id, "Введите номинал облигации в валюте(ПРИМЕР: Если 1000руб, то 1000)")
        bot.register_next_step_handler(message, what_basePrice)

def what_basePrice(message):
    global basePrice
    basePrice = message.text
    while type(basePrice) != float:
        try:
            basePrice = float(basePrice)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводи цифрами.')
            break

    if type(basePrice) != float or basePrice <= 0:
        bot.send_message(message.from_user.id, "Введите номинал облигации в валюте(ПРИМЕР: Если 1000руб, то 1000)")
        bot.register_next_step_handler(message, what_basePrice)
    else:
        bot.send_message(message.from_user.id, "Введите доходность купона облигации в процентах(ПРИМЕР: Если 7.5%, то 7.5)")
        bot.register_next_step_handler(message, what_bondCoupon)
    
def what_bondCoupon(message):
    global bondCoupon, only_float
    bondCoupon = message.text
    while type(bondCoupon) != float:
        try:
            bondCoupon = float(bondCoupon)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводи цифрами.')
            break

    if type(bondCoupon) != float or bondCoupon <= 0:
        bot.send_message(message.from_user.id, "Введите доходность купона облигации в процентах(ПРИМЕР: Если 7.5%, то 7.5)")
        bot.register_next_step_handler(message, what_bondCoupon)
    else:
        bot.send_message(message.from_user.id, "Введите укажите количество до погашения облигации(ПРИМЕР: Если 2 года 6 месяцев, то 2.6)")
        bot.register_next_step_handler(message, what_periodInAge)
    
def what_periodInAge(message):
    global periodInAge
    periodInAge = message.text
    while type(periodInAge) != float:
        try:
            periodInAge = float(periodInAge)
        except Exception:
            bot.send_message(message.from_user.id, 'Вводи цифрами.')
            break

    if type(periodInAge) != float or periodInAge <= 0:
        bot.send_message(message.from_user.id, "Введите доходность купона облигации в процентах(ПРИМЕР: Если 7.5%, то 7.5)")
        bot.register_next_step_handler(message, what_periodInAge)
    else:
        tmp_str0 = f"Доходность от разницы номинала: {round((((price/basePrice*100)-100)*-1), 2)}%"
        tmp_str1 = f"Доходность от разницы номинала c учетом НДФЛ 13%: {round(((((price/basePrice*100)-100)*-1)*0.87), 2)}%"
        tmp_str2 = f"Доходность от разницы номинала в год: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))), 2)}%"
        tmp_str3 = f"Доходность от разницы номинала в год с учетом НДФЛ 13%: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))*0.87), 2)}%"
        tmp_str4 = f"Общая доходность в год: {round((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+bondCoupon), 2)}%"
        tmp_str5 = f"Общая доходность в год с учетом НДФЛ 13%: {round(((((((price/basePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+bondCoupon)*0.87), 2)}%"
        tmp_str_list = [tmp_str0, tmp_str1, tmp_str2, tmp_str3, tmp_str4, tmp_str5]
        for i in range(6):
            bot.send_message(message.from_user.id, tmp_str_list[i])
    
bot.polling(none_stop=True)
