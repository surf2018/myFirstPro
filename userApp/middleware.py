
import traceback
from django.utils.deprecation import MiddlewareMixin
from django.db import DatabaseError,IntegrityError
from userApp.my_exception import MyException
from myFirstPro.common import response_failed
from django.http import HttpResponse

class MyExceptionMiddleware(MiddlewareMixin):
    def process_request(self,request):
        '''产生request对象之后，url匹配之前调用'''
        print('----process_request----')

    # def process_view(self, request, view_func, *view_args, **view_kwargs):
    #     '''url匹配之后，视图函数调用之前调用'''
    #     print('----process_view----')
    #     # view_func: url匹配到的视图函数。
    #     # return HttpResponse('process_view')

    def process_response(self,request,response):
        print('----process_response----')
        return response

    def process_exception(self, request, exception):
        '''视图函数发生异常时调用'''
        print(traceback.print_exc())
        if isinstance(exception,MyException):
            print("我定义的异常")
            return response_failed(exception.message)
        elif isinstance(exception,DatabaseError):
            print("数据库异常")
            return response_failed("数据库异常")
        elif isinstance(exception,IntegrityError):
            print(exception.message)
            return response_failed(exception.message)
        else:
            print("未知错误")
            return response_failed("未知错误")
