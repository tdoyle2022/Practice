from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
import json
import pprint
import os
from dotenv import load_dotenv

load_dotenv()
pp = pprint.PrettyPrinter(indent=2, depth=2)

# Create your views here.
def home(request):
    return render(request, 'pages/pokemon_form.html')

def pokemon(request):
    pokemon_name = request.POST.get('pokemon')

    authentication = OAuth1( os.environ['api_key'], os.environ['secret_key'] )
    endpoint = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(endpoint, auth=authentication)
    response_content = json.loads(response.content)
    # pp.pprint(response_content)
    img_url = response_content['icon']['preview_url']
    
    data = {
        'item_title' : pokemon_name,
        'img' : img_url 
    }
    
    return render(request, 'pages/pokemon.html', data)