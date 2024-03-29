# Generated by Django 3.2.3 on 2022-05-14 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_auto_20220514_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='shop_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='color',
            name='article',
            field=models.CharField(max_length=12, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='color',
            name='product_card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.product', verbose_name='Товар'),
        ),
        migrations.AlterField(
            model_name='product',
            name='age',
            field=models.IntegerField(choices=[(1, 'Женщина'), (2, 'Мужчина')], default=1, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(choices=[('Corneliani', 'Corneliani'), ('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Puma', 'Puma')], default='Corneliani', max_length=40, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='product',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Взрослый'), (2, 'Тинейджер'), (3, 'Ребенок')], default=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(default='', max_length=120, verbose_name='Материал'),
        ),
        migrations.AlterField(
            model_name='product',
            name='shop_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.shop', verbose_name='Магазин'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='auth_user_id',
            field=models.IntegerField(null=True, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='comp_name',
            field=models.CharField(max_length=120, verbose_name='Название'),
        ),
    ]
