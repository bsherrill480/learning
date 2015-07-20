from django.conf.urls import include, url
from .register_functions import registerUser
urlpatterns = [
    url(r'^', registerUser, name='web')
]