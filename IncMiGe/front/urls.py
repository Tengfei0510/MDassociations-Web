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
]
