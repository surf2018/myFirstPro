from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from myFirstPro.common import response_failed,response_succeess
# Create your views here.

def login(request):
    if(request.method=="POST"):
        name=request.POST['name']
        passwd=request.POST["passwd"]
        user=authenticate(username=name,password=passwd)
        if(user is not None):
            data={"name":name,"password":passwd}
            return response_succeess(data)
        else:
           return response_failed("输入错误的用户名和密码")

def register(request):
    if(request.method=="POST"):
        name=request.POST['name']
        passwd=request.POST["passwd"]
        # print(name,passwd)
        user=authenticate(username=name,password=passwd)
        if(user is not None):
            return response_failed("用户已经存在,请登录")
        else:
            #用户写入数据库
            result=User.objects.create_user(username=name,password=passwd)
            if result:
                data={"name":name,"password":passwd}
                return response_succeess(data)
            else:
                return response_failed("注册失败")
