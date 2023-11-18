from django.shortcuts import render
from .models import *

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})


def lesson_9(request):
    lessons = Lesson_9.objects.all()
    return render(request, 'lesson_9.html',{'lessons': lessons})

def mediauser(request):
    mediausers = MediaUser.objects.all()
    return render(request, 'lesson_9.html',{'mediausers': mediausers})