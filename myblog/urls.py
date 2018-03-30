from django.urls import path
from . import views

app_name = '[myblog]'
urlpatterns = [
    path('home/', views.home),
    path('home/android/', views.mAndroid, name='android'),
    path('home/testfrom/', views.testForm),

]
