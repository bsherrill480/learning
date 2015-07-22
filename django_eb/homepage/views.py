from django_eb.common.default_render import render

import logging

def homepage(request):
    user_logged_in = request.user.is_authenticated()
    context = {'name' : (request.user.username if user_logged_in else 'Word')}
    return render(request, 'homepage/index.html', context)
