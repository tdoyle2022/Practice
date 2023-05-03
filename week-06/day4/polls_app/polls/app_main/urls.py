from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
    path('view_poll', views.view_poll)
]