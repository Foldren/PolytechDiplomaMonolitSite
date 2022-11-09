# Generated by Django 3.2.3 on 2022-05-17 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0019_auto_20220517_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='shop_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='color',
            name='product_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.shop', verbose_name='Магазин'),
        ),
    ]