from django.contrib import admin
from django.urls import include, path
from polls import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path("", views.index),  
]