import config
import json
import os
import telebot
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def get_new_eng_word():
    url = 'http://eng.word.local.com/get/bot/word/'
    post_fields = {'foo': 'bar'}

    request = Request(url, urlencode(post_fields).encode())
    jsonData = urlopen(request).read().decode()    

    return json.loads(jsonData)['content']['message']


bot = telebot.TeleBot(config.token)


bot.send_message(271768203, get_new_eng_word())

@bot.message_handler(commands=['game'])
def geme(message):
    bot.send_message(message.chat.id, 'opa')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print(message.chat.id)
    bot.send_message(message.chat.id, message.text)
    
if __name__ == '__main__':
    bot.polling(none_stop=True)
