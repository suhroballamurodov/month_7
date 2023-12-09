from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.core.mail import send_mail
from .forms import ContactForm
from django.views.generic.edit import CreateView
from .models import *
from django.urls import reverse_lazy
 

def portfolio_details(request):
    return render(request, 'portfolio_details.html', {})

def main(request):
    return render(request, 'index.html', {})



# def sendmail(request):
#     send_mail(
#         subject='Bizning fake xabarni kutib oling',
#         message='Bizni guruh tomonidan yozildi',
#         from_email='suhrobbekallamurodov18@gmail.com',
#         recipient_list=['manajonovibrokhimjon@gmail.com'],
#         fail_silently=False,
#     )
#     return HttpResponse("Bizni yolg'on xabarni kutib oling")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')



''' Bu ikkinchi yo'l'''
# def contact(request):
#     form = ContactForm()

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             # Boshqa qanday ma'lumotlarni olish va validatsiya
#             # fuqarolarga xabar berish uchun
#             form = ContactForm()

#     return render(request, 'contact.html', {'form': form})

# def contact_success(request):
#     return render(request, 'contact_success.html')


# class ContactView(CreateView):
#     model = ContactModel
#     template_name = 'contact.html'
#     fields = ('ism','email','subyect','xabar')
#     success_url = reverse_lazy('contact_success')