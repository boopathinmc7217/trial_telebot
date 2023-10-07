"""import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import telebot

with open("my_token", "r") as e:
    bot_token = e.read().strip("\n")


bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start','Start'])
def handle_initial_setup(message):
    bot.send_message(message.chat.id, "enter you query")


@bot.message_handler(commands=["reminder"])
def handle_text_message(message):
    from datetime import datetime
    timestamp = message.date
    date_time = datetime.utcfromtimestamp(timestamp)
    formatted_date_time = date_time.strftime('%Y-%m-%d %H:%M:%S')

@bot.message_handler(func=lambda message: True)
def handle_text_message(message):
    bot.send_message(message.chat.id, "Hello, {}!".format(
        message.from_user.first_name))

@bot.message_handler(content_types=['photo'])
def handle_image_message(message):
    print(dir(message.photo[2]))
    bot.send_message(message.chat.id, "The file ID of the image is {}".format(
        message.photo[-1].file_size))
    
bot.polling()"""


API_TOKEN = "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"

import requests
api_end_point=""


def get_capital_of_india(openai_api_key):
    """Gets the capital of India using the OpenAI API.

    Args:
        openai_api_key: Your OpenAI API key.

    Returns:
        A string containing the capital of India.
    """

    headers = {
        "Authorization": f"Bearer {openai_api_key}"
    }

    data = {
        "prompt": "What is the capital of India?"
    }

    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions", headers=headers, json=data)

    output = response.json()

    return output


if __name__ == "__main__":
    openai_api_key = API_TOKEN

    capital_of_india = get_capital_of_india(openai_api_key)

    print(capital_of_india)
