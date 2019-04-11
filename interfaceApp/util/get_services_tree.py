from django.shortcuts import render
from django.views.generic import View
from userApp.my_exception import MyException
from django.contrib.sessions.models import Session
from interfaceApp.models.models import Service
from django.forms.models import model_to_dict
# Create your views here.
class ServerUtil:
    @classmethod
    def get_server_tree(self,parent):
        res=[]
        servers=Service.objects.filter(parent=parent)
        parent_name=""
        if parent!=0:
            object=Service.objects.get(pk=parent)
            parent_name=object.name
        for result in servers:
            nodeInfo=model_to_dict(result)
            nodeInfo['children']=ServerUtil.get_server_tree(nodeInfo['id'])
            nodeInfo['parent_name']=parent_name
            res.append(nodeInfo)
        return res
