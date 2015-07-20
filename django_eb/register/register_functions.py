from django_eb.common.logger import logger
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def registerUser(request):
    logger.debug(str(request.POST))
    try:
        fields = request.POST
        username = fields['username']
        password = fields['password']
        confirm_passowrd = fields['confirm-password']
        email = fields['email']
        user = User.objects.create_user(username, email, password)
    except:
        pass

    return HttpResponseRedirect("/")