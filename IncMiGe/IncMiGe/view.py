#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 11/1/16.
"""

from django.shortcuts import redirect


def index(request):
    return redirect('/front')
