# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    return render_to_response('index.html')
