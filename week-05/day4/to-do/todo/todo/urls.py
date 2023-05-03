"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
from django.urls import include, path
# from django.template import Context, loader
# from django.shortcuts import render

# def index(request):    
#     return render(request, '/Users/terrencedoyle/CodePlatoon/curriculum/week-05/day4/to-do/todo/index.html')

# def index(request):
#     template = loader.get_template(""))
#     return HttpResponse(template.render())

# def index(request):
#     response = HttpResponse("../index.html")
#     return response


urlpatterns = [
    path('admin/', admin.site.urls), # default admin routes, provided for free by django
    path('todo/', include('index.html'))
]

