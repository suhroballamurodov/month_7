from django.forms import ModelForm
from .models import Avto

class AvtoForm(ModelForm):
    class Meta:
        model = Avto
        fields = '__all__'