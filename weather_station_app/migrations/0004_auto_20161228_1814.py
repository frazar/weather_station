# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather_station_app', '0003_auto_20161228_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='description',
        ),
        migrations.AddField(
            model_name='channel',
            name='description',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]