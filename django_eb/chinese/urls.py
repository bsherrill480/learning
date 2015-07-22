from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^vocab/', views.chineseVocab, name='chineseVocab')
]