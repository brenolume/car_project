from django.contrib import admin
from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static # precisa ser importado para que seja possível usar imagens no projeto, caso contrário não será possível fazer upload de imagens para o banco de dados.
from cars.views import cars_view # importando a função cars_view do arquivo views.py, que é responsável por retornar a resposta para o usuário.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars_view)
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # aqui é adicionado o caminho para as imagens, para que seja possível fazer upload de imagens para o banco de dados.