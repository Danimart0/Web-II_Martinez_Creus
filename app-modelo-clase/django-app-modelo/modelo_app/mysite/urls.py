from django.contrib import admin
from django.urls import path, include
from mysite import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Aquí se carga la vista principal
    path('users/', include('users.urls')),  # Rutas para la app de usuarios
    path('polls/', include('polls.urls')),  # Rutas para la app de polls
]
