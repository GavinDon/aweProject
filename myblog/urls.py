from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'myblog'
urlpatterns = [
    path('home/', views.home),
    url('home/android/', views.mAndroid, name='android'),

]
