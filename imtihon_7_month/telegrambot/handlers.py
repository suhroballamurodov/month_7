import telebot
from telebot.types import Message
from telebot import types
import wikipedia, re
from dotenv import load_dotenv
load_dotenv()
import os


BOT_TOKEN =os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)


wikipedia.set_lang("uz")

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):    
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return '"Wikipedia"da bunday malumot mavjud emas!!'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Menga hohlagan habaringizni yuboring men uni wikipediadan topaman')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))