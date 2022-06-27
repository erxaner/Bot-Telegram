# pip install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot('masuk api disini')

# menghandle pesan /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # membalas pesan
    bot.reply_to(message, 'selamat datang di bot pertama saya')

# menghandel pesan /help
@bot.message_handler(commands=['help'])
def send_welcome(message):
    # membalas pesan
    bot.reply_to(message, 'Ada yang bisa dibantu?')
 
# memberitahukan bahwa bot telah mulai
print('bot start running')

while True:
    try:
        bot.polling()
    except:
        pass
