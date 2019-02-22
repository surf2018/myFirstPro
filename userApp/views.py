from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from myFirstPro.common import response_failed,response_succeess
import json
# Create your views here.

def login(request):
    if(request.method=="POST"):
        data=json.loads(request.body)
        if("name" in data and 'passwd' in data):
            name=data['name']
            passwd=data['passwd']
            print("username:"+name+" passwd:"+passwd)
            user=authenticate(username=name,password=passwd)
            if(user is not None):
                # data={"name":name,"password":passwd}
                return response_succeess(data)
            else:
                return response_failed("输入错误的用户名和密码")
        else:
            response_failed("参数错误")

def register(request):
    if(request.method=="POST"):
        data=json.loads(request.body)
        if ("name" in data and 'passwd' in data):
            name = str(data['name'])
            passwd = str(data['passwd'])
            print("username:" + name + " passwd:" + passwd)
            if(len(passwd)>=3 and len(passwd)<=20):
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
            else:
                return response_failed("密码必须是3到20个字符")
        else:
            response_failed("参数错误")
