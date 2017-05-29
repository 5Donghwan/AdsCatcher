from django.conf.urls import url
from .views import report, feedback


urlpatterns = [
    url(r'^report/$', report, name="report"),
    url(r'^feedback/$', feedback, name="feedback"),
]