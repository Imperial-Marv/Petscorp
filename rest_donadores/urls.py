from django.urls import path
from rest_donadores.views import Lista_Donadores, Borrar_Donador
from rest_donadores.viewslogin import token_login
urlpatterns = [
    path('Lista_Donadores', Lista_Donadores, name='Lista_Donadores'),
    path('Borrar_Donador/<id>', Borrar_Donador, name='Borrar_Donador'),
    path('token_login', token_login,name="token_login"),
]