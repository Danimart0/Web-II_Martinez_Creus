# urls.py del proyecto

from django.contrib import admin
from django.urls import include, path
from polls import views  # Esto es solo si quieres tener una vista 'index' de 'polls'

urlpatterns = [
    path("admin/", admin.site.urls),  # Ruta al panel de administración
    path("polls/", include("polls.urls")), 
    path("", views.index), 
    path('users/', include('users.urls'))

]
