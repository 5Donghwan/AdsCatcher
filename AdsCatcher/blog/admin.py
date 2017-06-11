from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'feed_title', 'content', 'created_at']

admin.site.register(Blog, BlogAdmin)