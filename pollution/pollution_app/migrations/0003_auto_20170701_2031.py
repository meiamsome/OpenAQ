# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollution_app', '0002_auto_20170701_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='pollution_app.City'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='pollution_app.Location'),
        ),
    ]
