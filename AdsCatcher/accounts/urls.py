from django.views.generic.base import TemplateView
from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views


urlpatterns = [
    # url(r'^login/$', login, name='login'),
    # #url(r'^logout/$', logout, {'next_page': 'gallery:index'}, name='logout'),
    url(r'^accounts/profile/', TemplateView.as_view(template_name = 'profile.html'))

]