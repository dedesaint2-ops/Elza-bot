import telebot
import random
import time
import threading
from datetime import datetime, timedelta

TOKEN = "8633167067:AAFcXmPWtpcg2DT5IJ5JltaVSyL1AhVDAX8"
CHAT_ID = "7000204425"

bot = telebot.TeleBot(TOKEN)

pairs = [
    "USD/PKR OTC 💎",
    "AUD/USD OTC 💎",
    "AUD/CAD OTC 💎",
    "USD/CHF OTC 💎",
    "EUR/CHF OTC 💎",
    "USD/JPY OTC 💎",
    "EUR/JPY OTC 💎"
]

martingale = 0

def get_entry_time():
    now = datetime.now()
    entry = now + timedelta(minutes=2)
    return entry.strftime("%H:%M")

def send_signal():
    global martingale

    while True:
        pair = random.choice(pairs)
        direction = random.choice(["BUY 📈", "SELL 📉"])
        entry = get_entry_time()

        msg = f"""
💎 VIP OTC SIGNAL 💎

📊 Pair: {pair}
📈 Direction: {direction}

⏰ Entry: {entry}
⏱️ Timeframe: M1
⌛ Expiration: 1 min

💰 Martingale: {'OFF' if martingale == 0 else f'MG{martingale}'}
"""

        bot.send_message(CHAT_ID, msg)

        # tann jis entry pase + trade fini (3 min total)
        time.sleep(180)

        result = random.choice(["WIN ✅", "LOSS ❌"])

        if result == "LOSS ❌":
            martingale += 1
        else:
            martingale = 0

        bot.send_message(CHAT_ID, f"📊 Result: {result}")

        # ti poz pou pa spam
        time.sleep(5)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🤖 VIP BOT ACTIVE 🔥")

threading.Thread(target=send_signal).start()

print("Bot VIP ap mache...")

bot.infinity_polling()
