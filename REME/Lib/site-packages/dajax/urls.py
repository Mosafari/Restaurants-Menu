# coding: utf-8
# Copyright (c) Alexandre Syenchuk (alexpirine), 2016

from __future__ import unicode_literals

from dajax import views
from django.conf.urls import url

app_name = 'dajax'
urlpatterns = [
    url(r'^get_url/(?P<url_name>.+)/$', views.get_url, name='get_url'),
]