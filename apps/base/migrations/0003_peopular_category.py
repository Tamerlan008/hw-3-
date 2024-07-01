# Generated by Django 5.0.6 on 2024-06-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_base_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peopular_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('description', models.CharField(max_length=255, verbose_name='Описание блюда')),
                ('photo', models.ImageField(upload_to='popular_category/', verbose_name='Фото блюда')),
            ],
            options={
                'verbose_name': 'Популярное категория',
                'verbose_name_plural': 'Популярное категория',
            },
        ),
    ]
