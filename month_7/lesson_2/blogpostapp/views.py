from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import PostModel
from .forms import PostForm
from django.views.generic.edit import CreateView
# Create your views here.

 
# def main(request):
#     return HttpResponse("Suhrob Allamurodov") 

# def ism_familiya(request):
#     return HttpResponse("<h1 style='color:green'>Suhrob Allamurodov</h1><h6>Suhrob Allamurodov</h6>")

# def manzil(request):
#     return HttpResponse(" <h4> Jizzax viloyati, Baxmal tumani</h4>")

# def malumot(request):
#     return HttpResponse("<h3>'Ipak yo'li' xalqaro turizm universiteti</h3>")

# def umumiy(request):
#     return HttpResponse({main},{ism_familiya}, {manzil}, {malumot})

# def lesson_3(request):
#     return render(request=request, template_name='test.html',context={})

# def sinov(request):
#     return render(request=request, template_name='sinov.html',context={})

def posts(request):
    posts = PostModel.objects.all()
    return render(request,'posts.html',{'posts':posts})


def post(request, pk):
    post = get_object_or_404(PostModel, id=pk)
    return render(request, 'post.html', context={'post':post})


def postdelete(request, pk):
    post = get_object_or_404(PostModel, id=pk)
    post.delete()
    return redirect('/posts')


def updatepost(request, pk):
    post = get_object_or_404(PostModel, id=pk)
    form = PostForm(initial={'title':post.title, 'short_desc':post.short_deck, 'body':post.body})
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('/posts')
    return render (request, 'update.html',context={'form':form})


def create_post(request):
    # post = get_object_or_404(PostModel)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
            form = PostForm()
    return render(request,'create_post.html',{'form':form})
