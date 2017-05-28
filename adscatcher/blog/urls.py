from django.conf.urls import url
from .views import index, reporting, feedback


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^reporting/$', reporting, name="reporting"),
    url(r'^feedback/$', feedback, name="feedback"),
]