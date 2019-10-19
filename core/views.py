from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1> Olá Mundo pelo Django, {nome} de {idade} Anos.! </h1>')
