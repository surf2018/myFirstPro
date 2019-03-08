from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from myFirstPro.common import response_failed,response_succeess
from django.contrib.sessions.models import Session
from userApp.forms import UserForm
import json
from django.views.generic import View
from userApp.my_exception import MyException

# Create your views here.

class UserView(View):
    def get(self,request,*args,**kwargs):
        token = request.META.get('HTTP_TOKEN', None)
        if(token is None or token=='null'):
            print("用户未登录")
            raise MyException("用户未登录")
            # return response_failed("用户未登陆")
        else:
            try:
            #h获取session后,在django的数据库里查询
                session=Session.objects.get(pk=token)
            except Session.DoesNotExist:
                raise MyException("session失效")
            #获取session 之后获取user id,获取所有已登录的用户
            else:
                user_id=session.get_decoded().get('_auth_user_id',None)
                if(user_id is None):
                    raise MyException("用户未找到")
                else:
                    try:
                        name=User.objects.get(pk=user_id).username
                    except User.DoesNotExist:
                        raise MyException("用户不存在")
                    else:
                        re={'name':name,'id':user_id}
                        print(str(re))
                        return response_succeess(str(re))
    def post(self,request,*args,**kwargs):
        data=json.loads(request.body)
        form = UserForm(data)
        if form.is_valid():
            name = data['username']
            passwd = data['password']
            #用户写入数据库
            user=User.objects.create_user(username=name,password=passwd)
            if user:
                login(request, user)
                session= request.session.session_key
                print("session:"+str(session))
                return response_succeess({'session':session})
            else:
                print(form.errors.as_json())
                raise MyException("注册失败")

        else:
            print(form.errors.as_json())
            raise MyException()
    def put(self,request,*args,**kwargs):
        data = json.loads(request.body)
        print("data" + str(data))
        form = UserForm(data)
        if form.is_valid():
            name = data['username']
            passwd = data['password']
            print("username:" + name + " passwd:" + passwd)
            user = authenticate(username=name, password=passwd)
            if user:
                login(request, user)
                session = request.session.session_key
                print("get session:" + str(session))
                return response_succeess({'session': session})

            else:
                raise MyException("登录失败")
        else:
            print(form.errors.as_json())
            raise MyException()
# def login(request):
#     if(request.method=="POST"):
#         data=json.loads(request.body)
#         print("data"+str(data))
#         form=UserForm(data)
#         if form.is_valid():
#             name=data['username']
#             passwd=data['password']
#             print("username:"+name+" passwd:"+passwd)
#             user=authenticate(username=name,password=passwd)
#             if user :
#                 loginu(request,user)
#                 session=request.session.session_key
#                 print("get session:"+str(session))
#                 return response_succeess({'session':session})
#
#             else:
#                 return response_failed("输入错误的用户名和密码")
#         else:
#             print(form.errors.as_json())
#             return response_failed("参数错误")
#
# def register(request):
#     if(request.method=="POST"):
#         data=json.loads(request.body)
#         form = UserForm(data)
#         if form.is_valid():
#             name = data['username']
#             passwd = data['password']
#             user=authenticate(username=name,password=passwd)
#             if user :
#                 return response_failed("用户已经存在,请登录")
#             else:
#                     #用户写入数据库
#                 user=User.objects.create_user(username=name,password=passwd)
#                 if user:
#                     loginu(request,user)
#                     session=request.session.session_key
#                     return response_succeess({'session':session})
#                 else:
#                     print(form.errors.as_json())
#                     return response_failed("注册失败")
#     else:
#         return response_failed("参数错误")
# def getUser(request):
#     #get header 信息
#     token=request.META.get('HTTP_TOKEN',None)
#     #h获取session后,在django的数据库里查询
#     session=Session.objects.get(pk=token)
#     #获取session 之后获取user id,获取所有已登录的用户
#     user_id=session.get_decoded().get('_auth_user_id',None)
#     name=User.objects.get(pk=user_id).username
#     re={'name':name,'id':user_id}
#     print(str(re))
#     return response_succeess(str(re))
