from django.contrib import admin
from .views import Blogpost
# Register your models here.

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'photos' )
    search_fields = ('title','created_at')


admin.site.register(Blogpost, BlogpostAdmin)