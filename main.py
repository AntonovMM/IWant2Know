import telebot

bot = telebot.TeleBot('1870466913:AAH6B4hKOhmcsX7xtFhPLUzq-5k09U15GSk')


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я Бот. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

    print(message.text + ' ' + message.chat.id)


@bot.message_handler(content_types=['document'])
def get_document_messages(message):
    print(message)


def bot_start():
    bot.polling(none_stop=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot_start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
