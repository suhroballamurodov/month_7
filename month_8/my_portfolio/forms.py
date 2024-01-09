from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['ism', 'email', 'subyekt','xabar']




''' Bu ikkinchi yo'l '''
# class ContactForm(forms.Form):
#     name = forms.CharField(label='Ismingiz')
#     email = forms.EmailField(label='Email manzilingiz')
#     subyekt = forms.CharField(label='Xabarni qisqacha mazmuni', widget=forms.Textarea)
#     xabar = forms.CharField(label='Xabaringiz', widget=forms.Textarea)
    

