# Generated by Django 5.1.3 on 2024-11-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_post',
            name='author',
            field=models.CharField(default='Автор неизвестен', max_length=50, verbose_name='Автор новости'),
        ),
    ]
