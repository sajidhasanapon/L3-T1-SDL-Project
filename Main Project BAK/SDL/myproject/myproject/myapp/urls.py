# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'myproject.myapp.views',
    url(r'^$', 'login', name='login'),
    url(r'^list/$', 'list', name='list'),
    url(r'^login/$', 'login', name='login'),
    url(r'^show/$', 'show', name = 'show'),
)