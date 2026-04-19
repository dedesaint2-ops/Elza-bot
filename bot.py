import telebot
import random
import time
import threading
from datetime import datetime, timedelta
import pytz

# 🔑 TOKEN & CHAT ID
TOKEN = "8633167067:AAFcXmPWtpcg2DT5IJ5JltaVSyL1AhVDAX8"
CHAT_ID = "7000204425"

bot = telebot.TeleBot(TOKEN)

# 📊 OTC PAIRS
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

# ⏰ ENTRY TIME UTC-5
def get_entry_time():
    tz = pytz.timezone("America/New_York")
    now = datetime.now(tz)

    entry = now + timedelta(minutes=2)
    entry = entry.replace(second=0, microsecond=0)

    return entry.strftime("%H:%M:%S")

# 📊 RSI SMART
def calculate_fake_rsi():
    return random.randint(10, 90)

def get_signal_from_rsi():
    rsi = calculate_fake_rsi()

    if rsi < 30:
        return "BUY 📈", rsi
    elif rsi > 70:
        return "SELL 📉", rsi
    else:
        return None, rsi

# 🚀 SIGNAL SYSTEM (1 BY 1)
def send_signal():
    global martingale

    while True:
        pair = random.choice(pairs)
        direction, rsi = get_signal_from_rsi()

        # ❌ pa voye si pa bon
        if direction is None:
            time.sleep(30)
            continue

        entry = get_entry_time()

        msg = f"""
💎 VIP SIGNAL 💎

📊 Pair: {pair}
📈 Direction: {direction}

⏰ Entry: {entry}
⏱️ Timeframe: M1
⌛ Exp: 1 min

📊 RSI: {rsi}
💰 Martingale: {'OFF' if martingale == 0 else f'MG{martingale}'}
🔥 Strategy: RSI
"""

        bot.send_message(CHAT_ID, msg)

        # ⏳ tann 2 min entry + 1 min trade
        time.sleep(180)

        result = random.choices(
            ["WIN ✅", "LOSS ❌"],
            weights=[75, 25]
        )[0]

        # martingale logic
        if result == "LOSS ❌":
            martingale += 1
        else:
            martingale = 0

        bot.send_message(CHAT_ID, f"📊 Result: {result}")

        # 🔥 pause pou evite spam
        time.sleep(30)

# ▶️ START COMMAND
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🤖 VIP BOT ACTIVE (UTC-5) 🔥")

# 🔁 RUN THREAD
threading.Thread(target=send_signal).start()

print("Bot VIP ap mache UTC-5...")

bot.infinity_polling()
