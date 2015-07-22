from django.conf.urls import include, url
from . import auth_functions
urlpatterns = [
    url(r'^register/', auth_functions.registerUser, name='register'),
    url(r'^login/', auth_functions.loginUser, name='login'),
    url(r'^logout/', auth_functions.logoutUser, name='logout'),

]