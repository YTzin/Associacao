from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=True)),
    path('admin/', admin.site.urls),
    path('pessoa/', include('pessoa.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
