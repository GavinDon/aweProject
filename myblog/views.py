from django.shortcuts import render
from django.http import HttpResponse
from myblog import models


# Create your views here.

def home(request):
    return render(request, 'home.html')


def mAndroid(request):
    return render(request, 'android.html')


def testForm(request):
    name = request.POST['mname']
    psw = request.POST['psw']
    isExit = models.user.objects.get_or_create(name=name, psw=psw)
    if isExit:
        return '已经存在信息'
    else:
        return '插入成功'

