from django.db import models


class Car(models.Model): # o nome da classe, é o nome da tabela que vai aparecer no banco de dados.
    id = models.AutoField(primary_key=True) # aqui será preenchido automaticamente a chave primária de cada carro cadastrado.
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)