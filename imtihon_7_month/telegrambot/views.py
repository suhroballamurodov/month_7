from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
import telebot
from .handlers import bot
import logging



def main(request):
    return render(request, 'index.html',{})

def home(request):
    return HttpResponse("Suhrob Allamurodovning django va bot ishlayotgan application 1")

@csrf_exempt
def index(request: HttpRequest):
    if request.method == 'GET':
        return HttpResponse("Telegram Bot")
    if request.method == 'POST':
        update = telebot.types.Update.de_json(
            request.body.decode("utf-8"))
        try:
            bot.process_new_updates([update])
        except Exception as e:
            logging.error(e)
        return HttpResponse(status=200)