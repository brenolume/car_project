from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # importação dos formulários de criação e autenticação de usuário do Django, que são utilizados para criar um novo usuário e fazer login no sistema.
from django.contrib.auth import authenticate, login, logout # é uma função pronta do django para autenticação do usuário
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login_view') # redirecionamento para a página de carros após o registro do usuário.
    else:
        user_form = UserCreationForm()
    return render(
        request, 
        'register.html', 
        {'user_form': user_form}
    ) # renderização da página de registro, passando o formulário de criação de usuário como contexto para a página.

def login_view(request):
    login_form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None: # se o usuário não for nulo.
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(
        request,
        'login.html',
        {'login_form': login_form}
    )

def logout_view(request):
    logout(request)
    return redirect('cars_list')
