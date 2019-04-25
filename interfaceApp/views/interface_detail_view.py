from django.shortcuts import render
from django.views.generic import View
from django.forms.models import model_to_dict
from userApp.my_exception import MyException
from interfaceApp.models.models import Service,IS_ROOT
from interfaceApp.models.interface import Interface
from myFirstPro.common import response_failed,response_succeess
import json
from interfaceApp.forms.ServiceForms import ServiceForm
from interfaceApp.forms.InterFaceForms import InterfaceForm
# Create your views here.
class InterfaceDetailView (View):
    def get(self, request, interface_id, *args, **kwargs):
        # 获取单个interfaces
        interface = Interface.objects.filter(id=interface_id)
        imp = model_to_dict(interface)
        return response_succeess(imp)
    def put(self, request, interface_id,*args, **kwargs):
        data = json.loads(request.body)
        print(data)
        form = InterfaceForm(data)
        print(form)
        if form.is_valid():
            update_Interface = Interface.objects.filter(id=interface_id).update(**form.cleaned_data)
            if (update_Interface):
                return response_succeess(update_Interface)
            else:
                return response_failed("更新interface数据库失败")
        else:
            print(form.errors)
            return response_failed("更新interface,表单验证失败")

    def delete(self, request,*args, **kwargs):
        print("删除interface")
        interface_id=request.path.split('/')[-1]
        del_interface= Interface.objects.filter(id=interface_id).delete()
        return response_succeess("删除接口成功")