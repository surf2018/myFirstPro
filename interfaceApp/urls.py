"""myFirstPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import views
from django.urls import path
from interfaceApp.views.service_list_view import service_list_view
from interfaceApp.views.service_detail_view import service_detail_view
urlpatterns = [
    path('service/',service_list_view.as_view()),
    path('service/<int:sid>',service_detail_view.as_view()),
    # path('getUser/',views.getUser),
]
