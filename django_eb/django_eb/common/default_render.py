from django.shortcuts import render as django_render
from . import user_functions
from .logger import logger
def render(request, template, context = None):
    if context is None:
        context = {}
    # user_logged_in = getUserLoggedIn()
    # logger.debug("homepage hit")
    if 'user_logged_in' not in context:
        context['user_logged_in'] = request.user.is_authenticated()
    return django_render(request, template, context)