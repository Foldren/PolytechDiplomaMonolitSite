# Generated by Django 3.2.3 on 2022-05-19 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0026_auto_20220519_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type_product',
            field=models.IntegerField(choices=[('Обувь', (('Кроссовки', 'Кроссовки'), ('Ботинки', 'Ботинки'))), ('Одежда', (('Платья', 'Платья'), ('Куртки', 'Куртки')))], default=False, verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='shop',
            name='description',
            field=models.CharField(default='', max_length=300, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='Добавьте описание', max_length=320, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='season',
            field=models.IntegerField(choices=[(1, 'Лето'), (2, 'Зима'), (3, 'Демисезон')], default=False, verbose_name='Сезон'),
        ),
    ]
