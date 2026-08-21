from django.http import request
from django.shortcuts import render # aqui é importado o render do django.shortcuts, que é responsável por renderizar o arquivo html e retornar a resposta para o usuário.
from cars.forms import CarForm
from cars.models import Car

def cars_view(request): # aqui é recebido o request do usuário, e é retornado a resposta para o usuário.
    cars = Car.objects.all()
    search_query = request.GET.get('search') # aqui é recebido o parâmetro de busca do usuário, que é passado através da url, e é armazenado na variável search_query.

    if search_query: # aqui verifica se a busca search foi feita, caso tenha sido feita, é feito um filtro no banco de dados, buscando todos os carros que contenham o parâmetro de busca passado pelo usuário.
        cars = cars.filter(model__contains=search_query) # aqui é feito um filtro no banco de dados, buscando todos os carros que contenham o parâmetro de busca passado pelo usuário, e é armazenado na variável cars.

    return render(
        request, #primeiro parâmetro que o render precisa receber é o request do usuário, que é recebido como parâmetro da função.
        'cars.html', #logo após o request, é necessário informar o nome do arquivo html que será renderizado, nesse caso, o arquivo cars.html.r 'Example Model'.
        { 'cars': cars }
    )

def new_cars_view(request):
    if request.method == 'POST': # aqui é verificado se o método da requisição é POST, caso seja, é criado um objeto da classe CarForm, que é responsável por criar o formulário de cadastro de carros, e é armazenado na variável new_car_form.
        new_car_form = CarForm(request.POST, request.FILES) # aqui é criado um objeto da classe CarForm, que é responsável por criar o formulário de cadastro de carros, e é armazenado na variável new_car_form.
    else:
        new_car_form = CarForm() # aqui é criado um objeto da classe CarForm, que é responsável por criar o formulário de cadastro de carros, e é armazenado na variável new_car_form.

    return render(
        request,
        'new_car.html',
        { 'new_cars_form': new_car_form } # aqui é passado o objeto new_car_form para o arquivo html, para que seja possível renderizar o formulário de cadastro de carros no arquivo html.
    )


