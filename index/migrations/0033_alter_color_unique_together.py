# Generated by Django 3.2.3 on 2022-05-21 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0032_alter_shop_yandex_rates_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='color',
            unique_together={('product_card', 'color')},
        ),
    ]
