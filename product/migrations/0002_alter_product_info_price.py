# Generated by Django 4.2.7 on 2024-04-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='price',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
        ),
    ]
