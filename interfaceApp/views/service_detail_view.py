from django.shortcuts import render
from django.views.generic import View
from interfaceApp.util.get_services_tree import ServerUtil
from userApp.my_exception import MyException
from django.contrib.sessions.models import Session
from interfaceApp.models import Service,IS_ROOT
from myFirstPro.common import response_failed,response_succeess
import json
from userApp.my_exception import MyException
from interfaceApp.forms.ServiceForms import ServiceForm
# Create your views here.
class service_detail_view (View):
    def put(self,request,*args,**kwargs):
        data = json.loads(request.body)
        form = ServiceForm(data)
        if form.is_valid():
            server_name = data['servername']
            server_desctiption = data['serverdesp']
            server_parent = data['parent']
            server = Service.objects.create(name=server_name, description=server_desctiption, parent=server_paren
        return response_succeess(servers)
    def post(self,request,*args,**kwargs):
        data=json.loads(request.body)
        form = ServiceForm(data)
        if form.is_valid():
            server_name=data['name']
            server_desctiption=data['description']
            server_parent=data['parent']
            server=Service.objects.create(name=server_name,description=server_desctiption,parent=server_parent)
            if server:
                return response_succeess('创建server成功')
            else:
                raise MyException("创建server异常")
        else:
            print(form.errors)
            return response_failed("创建server,表单验证失败")
