from django.shortcuts import render
import requests

def productos(request):
    url ='https://aara.duckdns.org/api.json'
    api = requests.get(url)
    api_rest = api.json()
    print(api_rest)
    return render(request,'galeria.html',{"api":api_rest})


