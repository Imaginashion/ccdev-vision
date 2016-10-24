# encoding: utf-8
from django.conf.urls import url
from userinterface.views import services, about

urlpatterns = [
    url(r'^about/$', about, name='ui-about'),
    url(r'^services/$', services, name='ui-services'),
]