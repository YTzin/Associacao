from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pessoa.urls')),  # Inclua o nome do seu aplicativo aqui
]
