# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('code', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=11)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=11)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollution_app.City')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter', models.CharField(max_length=6)),
                ('value', models.FloatField()),
                ('unit', models.CharField(max_length=10)),
                ('utc', models.DateTimeField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollution_app.Location')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollution_app.Country'),
        ),
    ]