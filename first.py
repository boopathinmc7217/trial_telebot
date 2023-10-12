from apscheduler.schedulers.background import BackgroundScheduler
import time
import telebot
import pandas as pd
from threading import Thread
CHAT_ID:any
with open("my_token", "r") as e:
    bot_token = e.read().strip("\n")
bot = telebot.TeleBot(bot_token)

file = ""
df = pd.read_excel(file)
rows, colums = df.shape
import random
unique_random_numbers = random.sample(range(0, rows + 1), rows+1)
quote_gen = (i for i in unique_random_numbers)

def quote_giver():
    quote_row = next(quote_gen)
    quote = df.iloc[quote_row, 0]
    category = df.iloc[quote_row, 1]
    return quote,category

@bot.message_handler()
def handle_initial_setup(message):
    global CHAT_ID
    CHAT_ID=message.chat.id
    quote,category=quote_giver()
    bot.send_message(
        message.chat.id, f" Hey {message.chat.username} \nQuote : \n {quote}\n Author : {category}")

@bot.message_handler(commands=["l"])
def handle_text_message(message):
    from datetime import datetime
    timestamp = message.date
    date_time = datetime.utcfromtimestamp(timestamp)
    formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
    print(message.venue)
    with open("data.json","r+") as e:
        bot.send_document(message.chat.id, e)


@bot.message_handler()
def handle_notification():
    now = time.localtime()
    quote, category = quote_giver()
    bot.send_message(CHAT_ID, f"Quote : \n {quote}\n Author : {category}")

scheduler = BackgroundScheduler()
scheduler.add_job(handle_notification, 'cron',hour=8,minute=20)
scheduler.start()
Thread(target=bot.polling()).start()




"""@bot.message_handler(func=lambda message: True)
def handle_text_message(message):
    bot.send_message(message.chat.id, "Hello, {}!".format(
        message.from_user.first_name))


@bot.message_handler(content_types=['photo'])
def handle_image_message(message):
    print(dir(message.photo[2]))
    bot.send_message(message.chat.id, "The file ID of the image is {}".format(
        message.photo[-1].file_size))"""
