from django.contrib import admin
from .models import News_post


@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели News_post."""
    list_display = ('title', 'author', 'pub_date', 'short_description')
    list_filter = ('pub_date', 'author')
    search_fields = ('title', 'short_description', 'text', 'author')
    date_hierarchy = 'pub_date'
