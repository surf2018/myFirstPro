from django.shortcuts import render
from django.views.generic import View
from interfaceApp.models import Service,IS_ROOT
from django.forms.models import model_to_dict
from interfaceApp.models.interface import Interface
from myFirstPro.common import response_failed,response_succeess
import json
from userApp.my_exception import MyException
from interfaceApp.forms.InterFaceForms import InterfaceForm
# Create your views here.
class InterfaceListView (View):
    #获取所有的接口列表
    def get(self,request,*args,**kwargs):
        ret=[]
        interfaces=Interface.objects.all()
        if interfaces:
            for i in interfaces:
                interface_dic=model_to_dict(i)
                ret.append(interface_dic)
        return response_succeess(ret)
    def post(self,request,*args,**kwargs):
        #创建接口
        data=json.loads(request.body)
        form = InterfaceForm(data)
        if form.is_valid():
            server=Service.objects.create(**form.cleaned_data)
            if server:
                return response_succeess('创建interface成功')
            else:
                raise MyException("创建interface异常")
        else:
            print(form.errors)
            return response_failed("创建interface,表单验证失败")
