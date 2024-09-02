from django.urls import path
from . import views
from .views import gerar_pdf_pessoa, filtar_pessoa
from .views import adicionar_conjuge, adicionar_dependente


urlpatterns = [
    path('home/', views.home, name='home'), 
    path('ver_pessoa/<int:id>/', views.ver_pessoa, name='ver_pessoa'),
    path('pessoa/<int:pessoa_id>/pdf/', gerar_pdf_pessoa, name='gerar_pdf_pessoa'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),

    
]
