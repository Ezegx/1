import telebot
import urllib.request
TOKEN = '5100179014:AAHGAxneELpzsVlBskcJTbyMveJn3CB1gvQ'
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.add(telebot.types.InlineKeyboardButton(text='получить', callback_data='/get'))
@bot.message_handler(commands=['start'])
def start_message(message):
    username = message.from_user.first_name
    bot.reply_to(message,f'Привет {username}!',reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '/get':
        getimg()
        photo = open('img.jpg', 'rb')
        bot.send_photo(call.message.chat.id, photo, reply_markup=keyboard)
    else:
        pass
def getimg():
    snapshot_address = 'http://10.0.0.10/webcapture.jpg?command=snap&channel=1'
    img = urllib.request.urlopen(snapshot_address).read()
    out = open('img.jpg', 'wb')
    out.write(img)
    out.close
bot.polling()