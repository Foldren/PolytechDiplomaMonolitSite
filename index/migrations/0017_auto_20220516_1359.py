# Generated by Django 3.2.3 on 2022-05-16 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20220514_1345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertising',
            options={'verbose_name': 'реклама', 'verbose_name_plural': 'Рекламные баннеры'},
        ),
        migrations.AlterField(
            model_name='advertising',
            name='shop_info',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='index.shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='color',
            name='color',
            field=models.IntegerField(choices=[(1, 'Черный'), (2, 'Зеленый'), (3, 'Синий'), (4, 'Красный'), (5, 'Белый')], default=1, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='color',
            name='product_card',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='index.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.IntegerField(choices=[(1, 'Взрослый'), (2, 'Тинейджер'), (3, 'Ребенок')], default=False, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Corneliani', 'Corneliani'), ('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Puma', 'Puma')], default=False, max_length=40, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Женщина'), (2, 'Мужчина')], default=False, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_info',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='index.shop', verbose_name='Магазин'),
        ),
    ]