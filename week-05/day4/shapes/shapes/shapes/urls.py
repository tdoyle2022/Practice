"""shapes URL Configuration

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
import math

def rootRouteHandler(request):
    response = HttpResponse("<h1>Welcome to the internet</h1>") # every request must receive one response
    print('=-=-=-=-=-=-=-=')
    print(dir(request))
    print('--------------')
    print(dir(response))
    print('=-=-=-=-=-=-=-=')
    return response


def anotherRouteHandler(request):
    response = HttpResponse("<marquee>We can make as many routes as we want</marquee>")
    response.status_code = 418

    # django automatically puts query string variables into a dictionary
    print(request.GET.get('format'))

    return response

def withParams(request, format='h1'):
    print(format)
    return HttpResponse(f"<{format}>Hello Django</{format}")


def recArea(request, height, width):
    area = height * width;
    try: response = HttpResponse(f"<h1>This is the area of your rectangle: {area}")
    except:
        response.status_code = 400
    return response

# def recArea(request):
#     height = request.GET.get('height')
#     width = request.GET.get('width')
#     area = int(height) * int(width)
#     response = HttpResponse(f"<h1>This is the area of your rectangle: {area}")
#     return response

def recPer(request, height, width):
    perimeter = 2*height + 2*width;
    response = HttpResponse(f"<h1>This is the perimeter of your rectangle: {perimeter}")
    return response

def cirArea(request, radius):
    area = math.pi * radius**2
    response = HttpResponse(f"<h1>This is the area of your circle: {area}")
    return response

def cirPer(request, radius):
    perimeter = 2 * math.pi * radius;
    response = HttpResponse(f"<h1>This is the perimeter of your circle: {perimeter}")
    return response

urlpatterns = [
    path('admin/', admin.site.urls), # default admin routes, provided for free by django
    path('', rootRouteHandler),
    path('another-route/', anotherRouteHandler),
    path('another-route/<str:format>', withParams),
    # path('rectangle/area/', recArea)
    path('rectangle/area/<int:height>/<int:width>', recArea),
    path('rectangle/perimeter/<int:height>/<int:width>', recPer),
    path('circle/area/<int:radius>', cirArea),
    path('circle/perimeter/<int:radius>', cirPer)
]
