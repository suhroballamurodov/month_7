from django.forms import ModelForm
from django import forms
from .models import PostModel

class PostForm(forms.ModelForm):
    class Meta:

        model = PostModel
        fields = '__all__'