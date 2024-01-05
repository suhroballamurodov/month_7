from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
import telebot
from .handlers import bot
import logging
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    return HttpResponse("Suhrob Allamurodovning django va bot birgalikda ishlayotgan application")



def sendmail(request):
    send_mail(
        subject='Imtihon uchun email yuborish', 
        message='N17 guruh Suhrob Allamurodov tomonidan yozildi...', 
        from_email='asunteam1824@mail.ru',
        recipient_list=['mamajonovibrokhimjon@gmail.com','suhrobbekallamurodov18@gmail.com'],
        fail_silently=False)
    return HttpResponse('Email has been sent!!...')



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