from django.urls import path
from .views import user_list
from . import views

urlpatterns = [
    path('', user_list, name='user_list'),
    path("create", views.createUserView, name="createuserView"),
    path("createUser", views.createUser, name="createUser"),
    path("detail/<int:id>", views.userDetail, name="userDetail"),
]