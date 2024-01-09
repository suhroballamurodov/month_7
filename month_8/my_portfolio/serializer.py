from rest_framework import serializers
from .models import ContactModel, Post

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactModel
        fields=('ism','email','subyekt','xabar')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
