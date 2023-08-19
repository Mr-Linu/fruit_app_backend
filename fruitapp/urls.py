from django.urls import path

from fruitapp import views

urlpatterns = [
    path('', views.home, name='home'),
]
