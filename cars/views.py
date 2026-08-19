from django.shortcuts import render # funcao do django que renderiza uma resposta HTTP e devolve uma `response`(resposta) para o usuario
from django.http import HttpResponse
from cars.models import Car

def cars_view(request): #(request) é obrigatório para qualquer view que solicite uma url no Django
    cars = Car.objects.all().order_by('-model') # queryset com todos os dados do objeto Car
    search = request.GET.get('search') # verifica se o usuario fez alguma busca
    if search:
        cars = cars.filter(model__icontains=search) #icontains faz com que a pesquisa filtre independente do case sensitive

    return render(
        request,
        'cars.html', 
        {'cars' : cars}
    )





