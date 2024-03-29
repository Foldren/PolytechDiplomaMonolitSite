# Generated by Django 3.2.3 on 2022-05-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_alter_color_color'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertising',
            options={'verbose_name': 'Реклама', 'verbose_name_plural': 'Рекламные баннеры'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Цвет товара', 'verbose_name_plural': 'Цвета продукции'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=40, verbose_name='Бренд'),
        ),
    ]
