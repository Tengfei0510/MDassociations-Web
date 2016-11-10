#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 10/30/16.
"""
from django.conf.urls import url

from . import views

app_name = 'web'

urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    url(r'^about$', views.about_view, name='about'),
    url(r'^browse/$', views.browse_view, name='browse'),
    url(r'^links/$', views.link_view, name='links'),
    url(r'^rcnmc/$', views.rcnmc_view, name='rcnmn'),
]
