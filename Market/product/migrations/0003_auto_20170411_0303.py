# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-11 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_sale_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_name', models.CharField(max_length=15)),
                ('Password', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default=1, max_length=1),
        ),
    ]
