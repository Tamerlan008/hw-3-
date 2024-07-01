# Generated by Django 5.0.6 on 2024-06-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_peopular_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our_chef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя Шеф Повара')),
                ('type', models.CharField(max_length=255, verbose_name='Тип повара')),
                ('photo', models.ImageField(upload_to='photo_chef/', verbose_name='Фото повара')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='facebook - повара')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='youtube - повара')),
            ],
            options={
                'verbose_name': 'Повар',
                'verbose_name_plural': 'Повара',
            },
        ),
    ]
