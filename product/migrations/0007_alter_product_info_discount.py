# Generated by Django 4.2.7 on 2024-04-09 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_product_info_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_info',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='In Percentage', max_digits=10, null=True),
        ),
    ]
