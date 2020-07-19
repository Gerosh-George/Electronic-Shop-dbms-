# Generated by Django 3.0.5 on 2020-04-23 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='finalorder',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]