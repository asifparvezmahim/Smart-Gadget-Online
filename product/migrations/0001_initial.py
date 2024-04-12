# Generated by Django 4.2.7 on 2024-04-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='product/images/')),
                ('details', models.TextField(max_length=500)),
                ('price', models.FloatField(default=None)),
                ('discount', models.CharField(help_text='input the percentage', max_length=5)),
                ('total_available_quantity', models.CharField(max_length=5000)),
                ('category', models.ManyToManyField(to='Category.product_category')),
            ],
        ),
    ]
