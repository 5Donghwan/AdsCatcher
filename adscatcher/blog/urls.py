from django.conf.urls import url
from .views import login_index


urlpatterns = [
    url(r'^$', login_index, name="login_index"),
]