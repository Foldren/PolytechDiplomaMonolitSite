# Generated by Django 3.2.3 on 2022-05-19 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0029_shop_yandex_rates_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='yandex_rates_id',
            field=models.BigIntegerField(default=None, verbose_name='Индекс яндекс отзывов'),
        ),
    ]
