from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

 
def main(request):
    return HttpResponse("Suhrob Allamurodov") 

def test(request):
    return render(request=request, template_name='test.html',context={})

def download(request):
    return render(request=request, template_name='download.html',context={})
