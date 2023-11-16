from django.shortcuts import render
# from django.http import HttpResponse

from .models import YangilikModel


def blogsayt(request):
    return render(request, template_name='blogsayt.html',context={})

def home(request):
    pass

def yangilik(request):
    news = YangilikModel.objects.all()
    # content = {
    #     'post': news,
    #     'title': "Bizning yangiliklarimiz"
    # }
    return render(request,'blogsayt.html', {'news':news,'title':'Bizning yangiliklar'})
