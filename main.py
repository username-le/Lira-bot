import telebot
from telebot import types


bot = telebot.TeleBot('5929320478:AAHKh3lGdwQyADvKcT8EQgSiWeCOc16nf-I')

deliv_25 = 0.175
deliv_30 = 0.182
deliv_40 = 0.196

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True) 
    btn1 = types.KeyboardButton("25%")
    btn2 = types.KeyboardButton("30%")
    btn3 = types.KeyboardButton("40%")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 
                     text="Привет, {0.first_name}! Я тестовый бот для расчета доставки. Нажмите на значок".format(message.from_user), 
                     reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "25%"):
        bot.send_message(message.chat.id, text='Введите сумму в лирах')
        bot.register_next_step_handler(message, deliver_25)
    elif(message.text == "30%"):
        bot.send_message(message.chat.id, text= 'Введите сумму в лирах')
        bot.register_next_step_handler(message, deliver_30)
    elif(message.text == "40%"):
        bot.send_message(message.chat.id, text= 'Введите сумму в лирах')
        bot.register_next_step_handler(message, deliver_40)
        
    
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("25%")
        button2 = types.KeyboardButton("30%")
        button3 = types.KeyboardButton("40%")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
        
def deliver_25(message):
        try:
#                 bot.send_message(message.chat.id, 'Цена в лари с доставкой: ')
                bot.send_message(message.chat.id, float(message.text) * deliv_25)
        except ValueError:
                bot.send_message(message.chat.id, 'Введите число')

def deliver_30(message):
        try:
#                 bot.send_message(message.chat.id, 'Цена в лари с доставкой: ')
                bot.send_message(message.chat.id, float(message.text) * deliv_30)
        except ValueError:
                bot.send_message(message.chat.id, 'Введите число')

def deliver_40(message):
        try:
#                 bot.send_message(message.chat.id, 'Цена в лари с доставкой: ')
                bot.send_message(message.chat.id, float(message.text) * deliv_40)
        except ValueError:
                bot.send_message(message.chat.id, 'Введите число')
                

bot.polling(none_stop=True)