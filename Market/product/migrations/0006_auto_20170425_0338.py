# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-25 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20170420_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to=b''),
        ),
    ]