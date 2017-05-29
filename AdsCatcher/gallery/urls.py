from django.conf.urls import url
from .views import gallery_list

urlpatterns = [
     url(r'^$', gallery_list, name="index"),
]

