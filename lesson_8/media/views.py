from django.shortcuts import render
from .models import *

def main(request):
    posts = Post.objects.all()
    return render(request, 'main.html', {'posts': posts})

def detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(render)


def lesson_9(request):
    lessons = Lesson_9.objects.all()
    return render(request, 'lesson_9.html',{'lessons': lessons})

def mediauser(request):
    mediausers = MediaUser.objects.all()
    print(mediausers)
    return render(request, 'lesson_9.html',{'mediausers': mediausers})

def lesson10(request):
    mediausers = MediaUser.objects.all()
    images = Rasmlar.objects.all()
    contacts = Contact.objects.all()
    abouts = Aboutme.objects.all()
    return render(request, 'uyga_vazifa.html',{'mediausers': mediausers,'images': images, 'abouts': abouts, 'contacts': contacts})


def about(request):
    abouts = Aboutme.objects.all()
    return render(request, 'about.html',{'abouts': abouts})


def images(request):
    images = Rasmlar.objects.all()
    return render(request, 'images.html',{'images': images})

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html',{'contacts': contacts})