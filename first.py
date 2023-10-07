from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot

with open("my_token", "r") as e:
    bot_token = e.read().strip("\n")


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def handle_initial_setup(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    weather_button = KeyboardButton('Time')
    markup.add(weather_button)
    bot.send_message(message.chat.id, "Select an option:", reply_markup=markup)


@bot.message_handler(commands=["l"])
def handle_text_message(message):
    from datetime import datetime
    timestamp = message.date
    date_time = datetime.utcfromtimestamp(timestamp)
    formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')
    print(message.venue)
    with open("data.json","r+") as e:
        bot.send_document(message.chat.id, e)

@bot.message_handler(func=lambda message: True)
def handle_text_message(message):
    bot.send_message(message.chat.id, "Hello, {}!".format(
        message.from_user.first_name))

@bot.message_handler(content_types=['photo'])
def handle_image_message(message):
    print(dir(message.photo[2]))
    bot.send_message(message.chat.id, "The file ID of the image is {}".format(
        message.photo[-1].file_size))
    
bot.polling()
