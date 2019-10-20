from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<h1> Olá Mundo pelo Django, {nome} de {idade} Anos.! </h1>')


def calculo(request, valor1, valor2):
    soma = valor2 + valor1
    subtracao = valor1 - valor2
    multiplicacao = valor1 * valor2
    divisao = valor1 / valor2
    return HttpResponse(f'<h2>Temos os valores: {valor1} e {valor2}</h2>'
                        f'<p>Valores Somados: {soma}\n'
                        f'<p>Valores Subtraidos: {subtracao}'
                        f'<p>Valores Multiplicados: {multiplicacao}\n'
                        f'<p>Valores divididos: {divisao}.')