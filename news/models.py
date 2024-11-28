from django.db import models

class News_post(models.Model):
    title = models.CharField('Название новости', max_length=50)  # Заголовок
    short_description = models.CharField('Краткое описание', max_length=200)  # Краткое описание
    text = models.TextField('Новость')  # Полный текст
    pub_date = models.DateTimeField('Дата публикации')  # Дата публикации
    author = models.CharField('Автор новости', max_length=50, default='Автор неизвестен')

    def __str__(self):
        return self.title  # Для отображения в админке

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
