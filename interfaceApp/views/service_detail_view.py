from django.shortcuts import render
from django.views.generic import View
from interfaceApp.util.get_services_tree import ServerUtil
from userApp.my_exception import MyException
from django.contrib.sessions.models import Session
from interfaceApp.models.models import Service,IS_ROOT
from interfaceApp.models.interface import Interface
from myFirstPro.common import response_failed,response_succeess
import json
from django.forms.models import model_to_dict
from userApp.my_exception import MyException
from interfaceApp.forms.ServiceForms import ServiceForm
# Create your views here.
class service_detail_view (View):
    def put(self,request,*args,**kwargs):
        server_id=(request.path).split("/")[-1]
        print(server_id)
        data = json.loads(request.body)
        print(data)
        form = ServiceForm(data)
        print(form)
        if form.is_valid():
            server_name = data['name']
            server_desctiption = data['description']
            server_parent = data['parent']
            new_server = Service.objects.filter(id=int(server_id)).update(name=server_name,description=server_desctiption, parent=server_parent)
            print("new_server"+str(new_server))
            if(new_server):
                return response_succeess(new_server)
            else:
                return response_failed("更新数据库失败")
        else:
            print(form.errors)
            return response_failed("更新server,表单验证失败")
    def delete(self,request,*args,**kwargs):
        print("删除sevice")
        server_id = (request.path).split("/")[-1]
        del_server=Service.objects.get(id=server_id)
        del_server.delete()
        return response_succeess("删除成功")
    def get(self,request,*args,**kwargs):
        print("获取服务的interface")
        s_id = (request.path).split("/")[-1]
        print(s_id)
        interface=Interface.objects.filter(service=s_id)
        ret=[]
        for result in interface:
            interfaceInfo=model_to_dict(result)
            ret.append(interfaceInfo)
        return response_succeess(ret)
