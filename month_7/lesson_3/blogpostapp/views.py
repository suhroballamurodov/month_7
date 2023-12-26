from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse 
from .models import PostModel
from .forms import PostForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

 
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



#Generic usuli

class PostListView(ListView):
    model = PostModel
    template_name = 'posts.html'
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        posts = PostModel.objects.all()
        context ['posts'] = posts
        return context


class PostDetailView(DetailView):
    model = PostModel
    template_name = 'post.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = PostModel
    template_name = 'create_post.html'
    fields = ('title', 'short_deck', 'body',)
    success_url = reverse_lazy('posts')


class PostUpdateView(UpdateView):
    model = PostModel
    fields = ('title','short_deck', 'body',)
    template_name = 'update.html'
    success_url = reverse_lazy('posts')


class PostDeleteView(DeleteView):
    model = PostModel
    template_name = 'delete.html'
    success_url = reverse_lazy('posts')






#Form usulu

#     def get(self, request, pk):
#         post = get_object_or_404(PostModel, id=pk)
#         return render (request, 'post.html', {'post':post})


    # def post(request, pk):
    #     post = get_object_or_404(PostModel, id=pk)
    #     return render(request, 'post.html', context={'post':post})


    # def postdelete(request, pk):
    #     post = get_object_or_404(PostModel, id=pk)
    #     post.delete()
    #     return redirect('/posts')


    # def updatepost(request, pk):
    #     post = get_object_or_404(PostModel, id=pk)
        # form = PostForm(initial={'title':post.title, 'short_desc':post.short_deck, 'body':post.body})
    #     if request.method == 'POST':
    #         form = PostForm(request.POST, instance=post)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('/posts')
    #     return render (request, 'update.html',context={'form':form})


    # def create_post(request):
    #     # post = get_object_or_404(PostModel)
    #     if request.method == 'POST':
    #         form = PostForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('posts')
    #     else:
    #             form = PostForm()
    #     return render(request,'create_post.html',{'form':form})
