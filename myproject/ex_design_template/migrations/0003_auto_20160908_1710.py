# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-08 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex_design_template', '0002_auto_20160908_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='price',
            field=models.FloatField(max_length=256, verbose_name='Price'),
        ),
    ]
