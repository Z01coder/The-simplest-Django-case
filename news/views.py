from django.shortcuts import render
from .models import News_post


def home(request):
    news = News_post.objects.all()  # Получаем все записи из модели News_post
    return render(request, 'news/news.html', {'news': news})  # Передаём их в шаблон

