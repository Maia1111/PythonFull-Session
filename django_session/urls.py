from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),   
    path("plataforma/", include('plataforma.urls')),
    path('', RedirectView.as_view(url='/auth/login/'), name='index_redirect'),  # Adicione esta linha
]
