# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-30 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20180829_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_date',
            field=models.DateField(null=True, verbose_name='出版日期'),
        ),
    ]