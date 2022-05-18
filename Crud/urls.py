"""Crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from CrudApp import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('', include("django.contrib.auth.urls")),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('add_collection/', views.add_collection, name='add_collection'),
    path('delete/<id>/', views.delete, name='delete'),
    path('edit/<id>/', views.edit, name='edit'),
    path('update/<id>/', views.update, name='update'),
    path('pie_chart/', views.pie_chart, name='pie_chart')
    #path('login/', LoginView.as_view(), name='login'),
]
