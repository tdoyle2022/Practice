import random
from django.shortcuts import render
import requests
import json

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def test(request):
    desired_pokemon = request.POST.get('pokemon')
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{desired_pokemon}/')
    response_content = json.loads(response.content)
    pokemon_type = response_content['types'][0]['type']['url']
    # second_pokemon = get_random_pokemon(pokemon_type)
    data = [{'image': response_content['sprites']['front_default']}]
    for x in range(5):
        data.append(get_random_pokemon(pokemon_type))
    return render(request, 'pages/pokemon_picture.html', {'data': data})

def get_random_pokemon(pokemon_type_url):
    response = requests.get(pokemon_type_url)
    response_content = json.loads(response.content)
    rand_poke = random.randint(0,len(response_content['pokemon']))
    response = requests.get(response_content['pokemon'][rand_poke]['pokemon']['url'])
    response_content = json.loads(response.content)
    return {'image': response_content['sprites']['front_default']}