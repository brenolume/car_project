from django.http import HttpResponse # importando a classe HttpResponse do Django, que é usada para retornar respostas HTTP para o usuário.

def cars_view(request): # aqui é recebido o request do usuário, e é retornado a resposta para o usuário.
    return HttpResponse("Hello, World!") # aqui é retornado a resposta para o usuário.






