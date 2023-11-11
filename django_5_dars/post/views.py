from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.

def main(request):
    return HttpResponse("Bizning veb saytimizdan to'liq foydalanishni istasangiz post sahifasiga o'ting")

def post(request):
    return render(request, template_name='.post/post.html', context={})

def index(request):
    post = Blogpost.objects.all()
    content = {
        'post': post,
        'title': "Veb sahifalarimiz"
    }
    # res = "<h1> Bizning veb saytimizdagi sahifalar bilan tanishing</h1>"
    # for item in post:
    #     res += f"<div>/n<p>{item.title}</p>/n<p>{item.content}</div></p><hr>/n"
    #     return HttpResponse(res)
    return render(request, template_name='post/post.html', context=content)