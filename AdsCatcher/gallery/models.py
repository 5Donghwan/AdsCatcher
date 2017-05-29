from django.conf import settings
from django.db import models

# Create your models here.
class Gallery(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30)
    contents = models.TextField()
    image = models.ImageField()
    count = models.IntegerField(default=0)

    def __str__(self):
        return '{}, {}'.format(self.title, self.id)