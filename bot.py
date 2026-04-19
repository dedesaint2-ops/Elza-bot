import telebot
import random
import time
import threading
from datetime import datetime, timedelta
import pytz

# 🔑 TOKEN & CHAT ID
TOKEN = "8633167067:AAFcXmPWtpcg2DT5IJ5JltaVSyL1AhVDAX8"
CHAT_ID = bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, "ID ou an parèt nan logs ✅")

bot = telebot.TeleBot(TOKEN)

# 📊 OTC PAIRS
pairs = [
    "USD/PKR OTC 💎", "EUR/USD OTC 💎", "GBP/USD OTC 💎",
    "USD/BDT OTC 💎",
    "AUD/USD OTC 💎", "AUD/CAD OTC 💎",
    "USD/CHF OTC 💎", "EUR/CHF OTC 💎",
    "USD/JPY OTC 💎", "EUR/JPY OTC 💎"
]

# 💰 MARTINGALE LEVEL
martingale_level = 0

# ⏰ ENTRY TIME +2 MIN
def get_entry_time():
    tz = pytz.timezone("America/New_York")
    now = datetime.now(tz)
    entry = (now + timedelta(minutes=2)).replace(second=0, microsecond=0)
    return entry.strftime("%H:%M:%S")

# ▶️ START
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🤖 Bot PRO OTC aktif 🔥")

# 📊 SIGNAL FUNCTION
def send_signal():
    global martingale_level

    while True:
        pair = random.choice(pairs)
        direction = random.choice(["BUY 📈", "SELL 📉"])
        entry_time = get_entry_time()

        signal = f"""
📊 SIGNAL OTC

Pair: {pair}
Direction: {direction}

⏰ Entry Time: {entry_time}
Timeframe: M1 ⏱️
Exp: 1 min

💰 Martingale Level: {martingale_level}
"""

        bot.send_message(CHAT_ID, signal)

        # ⏳ TANN 2 MIN (ENTRY) + candle fini
        time.sleep(125)

        result = random.choice(["WIN ✅", "LOSS ❌"])

        if result == "LOSS ❌":
            martingale_level += 1
        else:
            martingale_level = 0

        bot.send_message(CHAT_ID, f"📈 Result: {result}")

        # ⏳ RÈS TAN POU RIVE 3 MIN TOTAL
        time.sleep(55)

# 🔁 THREAD
threading.Thread(target=send_signal).start()

print("Bot ap mache...")

bot.infinity_polling() 
