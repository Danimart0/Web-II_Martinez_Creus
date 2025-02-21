from django.urls import path
from . import views

urlpatterns = [
    path("polls/", views.index, name="index"),         # Ruta para la vista index
    path("orders/", views.indexOrders, name="indexOrders"), 
]
