from django import forms # aqui é importado o forms do django, que é responsável por criar os formulários do django, e é utilizado para criar o formulário de cadastro de carros.
from cars.models import Brand, Car

class CarModelForm(forms.ModelForm): # porque Modelform? Porque o ModelForm é uma classe do Django que permite criar formulários a partir de modelos (models) do Django, facilitando a criação de formulários para criar ou atualizar registros no banco de dados. Ele automaticamente gera os campos do formulário com base nos campos do modelo, além de fornecer validação e métodos para salvar os dados no banco de dados. No caso do CarModelForm, ele é utilizado para criar um formulário baseado no modelo Car, permitindo que os usuários cadastrem novos carros no sistema.
    class Meta: # porque class Meta? porque a classe Meta é uma classe interna do Django que é utilizada para definir metadados para o modelo, como o nome da tabela no banco de dados, o nome do modelo, os campos que serão utilizados no formulário, entre outros. No caso do CarModelForm, a classe Meta é utilizada para definir que o modelo utilizado será o Car e que todos os campos do modelo serão utilizados no formulário.
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value') # aqui é utilizado o cleaned_data do django.forms, que é responsável por limpar os dados do formulário, e é utilizado para pegar o valor do campo value do formulário.
        if value < 20000:
            self.add_error('value', "O valor mínimo de carros deve ser de R$ 20.000,00") # aqui é utilizado o add_error do django.forms, que é responsável por adicionar um erro ao formulário, e é utilizado para adicionar um erro ao campo value do formulário, caso o valor seja menor que R$ 20.000,00.
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2000:
            self.add_error('factory_year', "Não é possível cadastrar carros fabricados antes de 2000")
        return factory_year