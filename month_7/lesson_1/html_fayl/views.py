from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def html(request):
    return render(request, 'index.html', {})

def base(request):
    return render(request, 'base.html', {})


def page1(request):
    return render(request, 'page1.html', {})

def page2(request):
    return render(request, 'page2.html', {})

def page3(request):
    return render(request, 'page3.html', {})

def page4(request):
    return render(request, 'page4.html', {})

def page5(request):
    return render(request, 'page5.html', {})

def page6(request):
    return render(request, 'page6.html', {})

