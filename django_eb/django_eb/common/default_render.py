from django.shortcuts import render as django_render
from . import user_functions
from .logger import logger
def render(request, template):
    # user_logged_in = getUserLoggedIn()
    # logger.debug("homepage hit")
    context = {'user_logged_in': user_functions.userLoggedIn()}
    return django_render(request, template, context)