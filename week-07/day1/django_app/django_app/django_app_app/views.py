from django.shortcuts import render
from . import views
import random
from django.db.models import Q

users = {}
# Create your views here.
def index(request):
    user_id = request.COOKIES.get('user_id')
    if not user_id:
        user_id = str(random.randint(1, 10000))
        response = render(request, 'pages/index.html', {'visits': 1})
        response.set_cookie('user_id', user_id)
        users[user_id] = 1
        return response
    
    if user_id in users:
        users[user_id] += 1
    else:
        users[user_id] = 1

    visits = users[user_id]
    return render(request, 'pages/index.html', {'visits': visits})

                          


