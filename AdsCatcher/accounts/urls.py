from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': 'gallery:index'}, name='logout'),
]