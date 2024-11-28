from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='news_home'),  # Главная страница приложения
]
