from django.shortcuts import render
from django.views.generic import View
from interfaceApp.models.interface import Interface
from django.forms.models import model_to_dict
from myFirstPro.common import response_failed,response_succeess
import json
from userApp.my_exception import MyException

# Create your views here.
class ServiceInterfacesView (View):
    def get(self,request,*args,**kwargs):
        #获取单个服服务的interfaces
        sid=request.path.split('/')[3]
        print(sid)
        ret=[]
        server_interfaces=Interface.objects.filter(service=sid)
        for i in server_interfaces:
            interface=model_to_dict(i)
            ret.append(interface)
        return response_succeess(ret)
