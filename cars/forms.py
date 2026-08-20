from django import forms # aqui é importado o forms do django, que é responsável por criar os formulários do django, e é utilizado para criar o formulário de cadastro de carros.
from cars.models import Brand, Car

class CarForm(forms.Form): 
    model = forms.CharField(max_length=100)
    brand = forms.ModelChoiceField(Brand.objects.all()) # aqui é criado um campo de escolha de marca, que é preenchido com todas as marcas cadastradas no banco de dados, utilizando o ModelChoiceField do django.forms, que é responsável por criar um campo de escolha baseado em um modelo do django.
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField() # aqui é criado um campo de upload de imagem, que é utilizado para fazer o upload da foto do carro, utilizando o ImageField do django.forms, que é responsável por criar um campo de upload de imagem.