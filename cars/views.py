from django.shortcuts import render
from cars.models import Car

def cars_view(request): #(request) é obrigatório para qualquer view que solicite uma url no Django
    cars = Car.objects.all()
    
    return render(
        request, # render é a função 
        'cars.html', 
        {'cars' : cars }
    )