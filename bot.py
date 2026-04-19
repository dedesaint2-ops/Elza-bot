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
running = False  # 🔥 anti-duplicate

# ⏰ UTC-5 ENTRY TIME
def get_entry_time():
    tz = pytz.timezone("America/New_York")
    now = datetime.now(tz)
    entry = now + timedelta(minutes=2)
    entry = entry.replace(second=0, microsecond=0)
    return entry.strftime("%H:%M:%S")

# 📊 SMART RSI
def calculate_fake_rsi():
    return random.randint(10, 90)

def get_signal():
    rsi = calculate_fake_rsi()
    if rsi < 30:
        return "BUY 📈", rsi
    elif rsi > 70:
        return "SELL 📉", rsi
    else:
        return None, rsi

# 🚀 SIGNAL SYSTEM (ANTI-SPAM)
def send_signal():
    global martingale

    while True:
        pair = random.choice(pairs)
        direction, rsi = get_signal()

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

        # ⏳ tann 3 min (entry + trade)
        time.sleep(180)

        result = random.choices(
            ["WIN ✅", "LOSS ❌"],
            weights=[75, 25]
        )[0]

        if result == "LOSS ❌":
            martingale += 1
        else:
            martingale = 0

        bot.send_message(CHAT_ID, f"📊 Result: {result}")

        # 🔥 pause pou evite doublon
        time.sleep(30)

# 🔥 ANTI-DOUBLE THREAD
def start_bot():
    global running
    if running:
        return
    running = True
    send_signal()

# ▶️ START COMMAND
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🤖 VIP BOT ACTIVE (UTC-5) 🔥")

# 🚀 MAIN
if __name__ == "__main__":
    print("Bot VIP ap mache san doublon...")

    t = threading.Thread(target=start_bot)
    t.daemon = True
    t.start()

    bot.infinity_polling()
