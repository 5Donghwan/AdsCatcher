from django.conf.urls import url
from .views import report_new, feedback_new


urlpatterns = [
    url(r'^report/$', report_new, name="report_new"),
    url(r'^feedback/$', feedback_new, name="feedback_new"),
]