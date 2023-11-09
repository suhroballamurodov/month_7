from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main(request):
    return HttpResponse("<h1 textcolor='red' align='center'>Bizning avto market haqida to'liq ma'lumt olmoqchi bo'lsangiz avto sahifasiga o'ting</h1>")


def avto(request):
    return HttpResponse("BMW-X6")


def handler404(request, exception):
    return HttpResponse("<h1 align='center'> 404 </h1> <br> <h4 align='center'><b>Uzr siz qidirgan sahifani topa olmadik</h4>")