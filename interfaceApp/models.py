from django.db import models
from interfaceApp.fields.form.object_field import ObjectField
# Create your models here.'
IS_ROOT=0
class Service(models.Model):
    name = models.CharField('name', blank=False, default="", max_length=200)
    description = models.TextField('description', blank=True, default='')
    parent = models.IntegerField('父节点', blank=False, default=IS_ROOT)

    def __str__(self):
        return self.name
class Interface(models.Model):

    name = models.CharField('name', blank=False, max_length=200)
    description = models.TextField('description', default='')

    host = models.CharField('host', default="", max_length=200)
    url = models.CharField('url', blank=False, max_length=500)
    method = models.CharField('method', blank=False, max_length=20)
    header = ObjectField('header', default={})
    parameter = ObjectField('parameter', default={})
    parameter_type = models.CharField('parameter_type, json or form', default="json", max_length=20)
    response = ObjectField('response', default="")
    response_type = models.CharField('response_type, json or html', default="json", max_length=20)
    assertion = ObjectField('assertion', default=[])
    service = models.ForeignKey(Service, blank=False, related_name='service_interfaces', on_delete=models.SET_DEFAULT,
                                default=0)

