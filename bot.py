import os
import schedule
import time
import random
from telegram import Bot

TOKEN = os.environ.get('TOKEN', '8758892168:AAFrpv4wwWXswawm6w4j-VJ-MSfZ1wDOfPo')
CHANNEL_ID = os.environ.get('CHANNEL_ID', '-1003027136216')

FACTS = [
    "Пчелы могут распознавать человеческие лица. Они используют тот же принцип, что и люди.",
    "Осьминоги имеют три сердца и голубую кровь.",
    "Самое большое дерево в мире — секвойя Генерал Шерман.",
    "Муравьи могут поднимать вес, в 50 раз превышающий их собственный.",
    "Бабочки пробуют пищу ногами.",
    "Средний человек за свою жизнь съедает около 35 тонн еды.",
    "Дельфины спят с одним открытым глазом.",
    "Солнце составляет 99,86% всей массы Солнечной системы.",
    "Пингвины предлагают друг другу камешки в качестве предложения брака.",
    "В человеческом теле больше бактерий, чем клеток."
]

bot = Bot(token=TOKEN)

def send_fact():
    fact = random.choice(FACTS)
    hashtags = random.choice(["#интересныефакты #наука", "#факты #природа", "#интересно #знания"])
    emoji = random.choice(["🧠", "🌟", "💡", "🔬"])
    message = f"{emoji} Интересный факт:\n\n{fact}\n\n{hashtags}"
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=message)
    except Exception as e:
        print(f"Ошибка: {e}")

def main():
    send_fact()
    schedule.every().dat.at("19:00").do(send_fact)
    print("Бот запущен!")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()