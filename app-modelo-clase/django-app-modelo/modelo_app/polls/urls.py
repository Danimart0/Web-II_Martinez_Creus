from django.urls import path
from . import views

urlpatterns = [
    path("polls/", views.index, name="indexpolls"),         # Ruta para la vista index
    path("orders/", views.indexOrders, name="indexOrders"), 
]
