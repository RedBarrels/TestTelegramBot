import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text in "Privet":
        bot.send_message(message.chat.id, "Shalom!")
    else:
        bot.send_message(message.chat.id, "Ne ponimay")

if __name__ == '__main__':
     bot.polling(none_stop=True)