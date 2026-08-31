from django.http import request
from django.shortcuts import render, redirect # aqui é importado o render do django.shortcuts, que é responsável por renderizar o arquivo html e retornar a resposta para o usuário.
from cars.forms import CarModelForm  # aqui é importado o CarModelForm do arquivo forms.py, que é responsável por criar o formulário de cadastro de carros, e é utilizado para criar o formulário de cadastro de carros.
from cars.models import Car

def cars_view(request): # aqui é recebido o request do usuário, e é retornado a resposta para o usuário.
    cars = Car.objects.all()
    search_query = request.GET.get('search') # aqui é recebido o parâmetro de busca do usuário, que é passado através da url, e é armazenado na variável search_query.

    if search_query: # aqui verifica se a busca search foi feita, caso tenha sido feita, é feito um filtro no banco de dados, buscando todos os carros que contenham o parâmetro de busca passado pelo usuário.
        cars = cars.filter(model__contains=search_query) # aqui é feito um filtro no banco de dados, buscando todos os carros que contenham o parâmetro de busca passado pelo usuário, e é armazenado na variável cars.

    return render(
        request, #primeiro parâmetro que o render precisa receber é o request do usuário, que é recebido como parâmetro da função.
        'cars.html', #logo após o request, é necessário informar o nome do arquivo html que será renderizado, nesse caso, o arquivo cars.html.r 'Example Model'.
        { 'cars': cars } # o que acontece aqui é que o render vai pegar o arquivo cars.html e vai passar para ele o dicionário cars, que contém todos os carros que foram buscados no banco de dados, e vai renderizar o arquivo html com os carros que foram buscados no banco de dados.
    )

def new_cars_view(request):
    if request.method == 'POST': # aqui é verificado se o método da requisição é POST, caso seja, é criado um objeto da classe CarForm, que é responsável por criar o formulário de cadastro de carros, e é armazenado na variável new_car_form.
        new_car_form = CarModelForm(request.POST, request.FILES) # aqui é criado um objeto da classe CarForm, que é responsável por criar o formulário de cadastro de carros, e é armazenado na variável new_car_form.
        if new_car_form.is_valid(): # aqui é verificado se o formulário de cadastro de carros é válido, caso seja, é criado um objeto da classe Car, que é responsável por criar um novo carro no banco de dados, e é armazenado na variável new_car.
            new_car_form.save() # aqui é chamado o método save do objeto new_car_form, que é responsável por salvar o novo carro no banco de dados.
            return redirect ('cars_list') # aqui é feito um redirecionamento para a página de listagem de carros, caso o formulário de cadastro de carros seja válido e o novo carro seja salvo no banco de dados.
    else:
        new_car_form = CarModelForm()

    return render(
        request,
        'new_car.html',
        { 'new_cars_form': new_car_form } # aqui é passado o objeto new_car_form para o arquivo html, para que seja possível renderizar o formulário de cadastro de carros no arquivo html.
    )


