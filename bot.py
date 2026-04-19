import telebot
import random
import time
from datetime import datetime, timedelta
import pytz

TOKEN = "8633167067:AAFcXmPWtpcg2DT5IJ5JltaVSyL1AhVDAX8"
CHAT_ID = "7000204425"

bot = telebot.TeleBot(TOKEN)

pairs = [
    "AUD/USD OTC 💎",
    "AUD/CAD OTC 💎",
    "USD/CHF OTC 💎",
    "EUR/CHF OTC 💎",
    "USD/JPY OTC 💎",
    "EUR/JPY OTC 💎"
]

martingale = 0
last_signal_time = None  # 🔒 LOCK

def get_entry_time():
    tz = pytz.timezone("America/New_York")
    now = datetime.now(tz)
    entry = now + timedelta(minutes=2)
    entry = entry.replace(second=0, microsecond=0)
    return entry.strftime("%H:%M:%S")

def get_signal():
    rsi = random.randint(10, 90)
    if rsi < 30:
        return "BUY 📈", rsi
    elif rsi > 70:
        return "SELL 📉", rsi
    return None, rsi

def run_bot():
    global martingale, last_signal_time

    print("Bot anti-spam ap mache...")

    time.sleep(20)

    while True:
        now = time.time()

        # 🔒 BLOKE SI LI TWÒ BONÈ
        if last_signal_time and (now - last_signal_time < 180):
            time.sleep(5)
            continue

        pair = random.choice(pairs)
        direction, rsi = get_signal()

        if direction is None:
            time.sleep(10)
            continue

        entry = get_entry_time()

        msg = f"""
💎 VIP SIGNAL 💎

📊 Pair: {pair}
📈 Direction: {direction}

⏰ Entry: {entry}
⏱️ M1 | Exp: 1 min

📊 RSI: {rsi}
💰 Martingale: {'OFF' if martingale == 0 else f'MG{martingale}'}
"""

        bot.send_message(CHAT_ID, msg)

        # 🔒 SAVE TIME
        last_signal_time = time.time()

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

        time.sleep(30)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🤖 BOT ACTIVE 🔥")

if __name__ == "__main__":
    import threading
    threading.Thread(target=bot.infinity_polling, daemon=True).start()
    run_bot()
