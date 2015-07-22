from django_eb.common.logger import logger
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def registerUser(request):
    logger.debug(str(request.POST))
    try:
        fields = request.POST
        username = fields['username']
        password = fields['password']
        confirm_password = fields['confirm-password']
        email = fields['email']
        user = User.objects.create_user(username, email, password)
        logger.debug(user)
    except Exception as e:
        logger.debug("NO USER MADE: {}".format(e))
        raise e
    return HttpResponseRedirect("/")

def loginUser(request):
    logger.debug(str(request.POST))
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    except Exception as e:
        logger.debug("NO USER MADE: {}".format(e))
        raise e
    return HttpResponseRedirect("/")

def logoutUser(request):
    logout(request)
    logger.debug('Logged out user')
    return HttpResponseRedirect("/")