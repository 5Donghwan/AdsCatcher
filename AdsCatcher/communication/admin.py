from django.contrib import admin
from .models import Report, Feedback
# Register your models here.


class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'contents', 'author', 'created_at']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']


admin.site.register(Report, ReportAdmin)
admin.site.register(Feedback, FeedbackAdmin)