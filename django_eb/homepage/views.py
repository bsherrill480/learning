from django.http import HttpResponse
from django_eb.common.default_render import render
from django.shortcuts import render as django_render

import logging

def homepage(request):
    user_logged_in = False
    return render(request, 'homepage/index.html')
