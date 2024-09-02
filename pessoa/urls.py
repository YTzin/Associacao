from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Roteia a URL base para a visualização home
    path('home/', views.home, name='home'),
    path('ver_pessoa/<int:id>/', views.ver_pessoa, name='ver_pessoa'),
    path('pessoa/<int:pessoa_id>/pdf/', views.gerar_pdf_pessoa, name='gerar_pdf_pessoa'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
]
