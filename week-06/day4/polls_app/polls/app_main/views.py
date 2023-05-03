from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    Homepage
    """
    return HttpResponse("hello world, app main index.")

def view_poll(request):
    """
    View a poll
    """
    
