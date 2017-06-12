from django.db import models


# Create your models here.
class Blog(models.Model):
    page_name = models.CharField(max_length=30)
    feed_title = models.CharField(max_length=300)
    content = models.CharField(max_length=600)
    created_at = models.CharField(max_length=30)
    state = models.CharField(max_length=10, default="")