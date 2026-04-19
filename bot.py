import telebot

TOKEN = "8633167067:AAFcXmPWtpcg2DT5IJ5JltaVSyL1AhVDAX8"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot la ap mache ✅")

bot.infinity_polling()
