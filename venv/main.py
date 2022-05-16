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
"""
Price = int (input("Введите стоимость облигации(в валюте):")) 
BasePrice = int (input("Введите номинал облигации(в валюте):")) 
BondCoupon = float (input("Введите доходность купона облигации(в процентах):")) 
periodInAge = float (input("Введите укажите количество до погашения облигации(пример 2 года 6 месяцев = 2.6):")) 
print("Доходность от разницы номинала=", ((Price/BasePrice*100)-100)*-1) 
print("Доходность от разницы номинала c учетом НДФЛ 13%=", (((Price/BasePrice*100)-100)*-1)*0.87) 
print("Доходность от разницы номинала в год=",((((Price/BasePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))) 
print("Доходность от разницы номинала в год с учетом НДФЛ 13%=",((((Price/BasePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))*0.87) 
print("Общая доходность в год=",((((Price/BasePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+BondCoupon) 
print("Общая доходность в год с учетом НДФЛ 13%=",(((((Price/BasePrice*100)-100)*-1)/(periodInAge//1+periodInAge%1/12*10))+BondCoupon)*0.87)
"""
