from django.conf.urls import url
from .views import login_index, report, feedback


urlpatterns = [
    url(r'^$', login_index, name="login_index"),
    url(r'^report/$', report, name="report"),
    url(r'^feedback/$', feedback, name="feedback"),
]