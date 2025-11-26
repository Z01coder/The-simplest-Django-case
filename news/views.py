from django.shortcuts import render
from .models import News_post


def home(request):
    """Главная страница с отображением всех новостей."""
    news = News_post.objects.all().order_by('-pub_date')  # Получаем все записи, отсортированные по дате
    return render(request, 'news/news.html', {'news': news})  # Передаём их в шаблон

