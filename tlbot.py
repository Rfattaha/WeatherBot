from telebot import types
import telebot
from weather import *

bot = telebot.TeleBot("TOKEN", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN



kb = types.InlineKeyboardMarkup(row_width=2)

words = [
'London' ,
'Istanbul',
'Moscow' ,
'Berlin',
'Type' 
]


for item in words:
    kb.add(types.InlineKeyboardButton(item, callback_data = item))



@bot.message_handler(commands=['start', 's'])
def post_random_article(message):
    word = 'Select the city'
    bot.send_message(message.from_user.id, word, reply_markup = kb)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
  message_text = message.text 
  cid = message.chat.id
  bot.send_message(text=getResp(message_text),chat_id=cid)
  


@bot.callback_query_handler(func=lambda call:True )
def handle_query(call):
   if call.data == "Type":
       bot.send_message(call.from_user.id, 'Please Enter The City : ')
   else:
        bot.send_message(call.from_user.id,getResp(call.data))



bot.infinity_polling()
