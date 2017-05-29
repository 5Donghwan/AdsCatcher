from django.conf.urls import url
from .views import index, gallery_new, gallery_list

urlpatterns = [
     url(r'^$', index, name="index"),
    url(r'^new/$', gallery_new, name="gallery_new"),
     url(r'^list/$', gallery_list, name="gallery_list"),
]

