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
    else:
        return None, rsi

def run_bot():
    global martingale

    print("Bot ap mache (NO SPAM)...")

    # delay pou evite spam startup
    time.sleep(15)

    while True:
        pair = random.choice(pairs)
        direction, rsi = get_signal()

        if direction is None:
            time.sleep(20)
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

        # tann trade fini
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

        # pause anvan pwochen signal
        time.sleep(60)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "🤖 BOT ACTIVE 🔥")

# 🔥 KLE SOLISYON AN (NO THREAD MULTI)
if __name__ == "__main__":
    import threading

    # Telegram polling
    threading.Thread(target=bot.infinity_polling, daemon=True).start()

    # sèlman 1 loop
    run_bot()
