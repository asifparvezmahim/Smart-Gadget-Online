# Generated by Django 4.2.7 on 2024-04-08 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_info_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='discount',
            field=models.CharField(help_text='input the percentage', max_length=5),
        ),
    ]
