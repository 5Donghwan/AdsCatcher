from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'page_name', 'feed_title', 'content', 'created_at', 'state']

admin.site.register(Blog, BlogAdmin)