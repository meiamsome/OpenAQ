# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollution_app', '0003_auto_20170701_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=7, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=7, max_digits=11, null=True),
        ),
    ]
