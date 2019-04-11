
import json

from django.db import models
import ast


class ObjectField(models.TextField):
    description = "Stores a python dict"
    def __init__(self, *args, **kwargs):
        super(ObjectField, self).__init__(*args, **kwargs)

    def to_python(self, value):#to_python 函数用于转化数据库中的字符到 Python的变量，
        if not value:
            value = {}
            return value
        if isinstance(value, dict):
            return value
        try:
            ret=json.loads(value)
        except:
            ret={}
            return ret
        else:
            return ret

    def get_prep_value(self, value):#用于将Python变量处理后(此处为压缩）保存到数据库，使用和Django自带的 Field 一样。
        if value is None:
            return value
        return json.dumps(value,ensure_ascii=False)

    def from_db_value(self, value,expression,connection,context):#from_db_value 函数用于转化数据库中的字符到 Python的变量
        if not value:
            value = {}
            return value
        if isinstance(value, dict):
            return value
        try:
            ret=json.loads(value)
        except:
            ret={}
            return ret
        else:
            return ret