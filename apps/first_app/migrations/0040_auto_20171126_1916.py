# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 03:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0039_auto_20171126_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='buying_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 26, 19, 16, 16, 728016)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='current_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 26, 19, 16, 16, 728016)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='past_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 26, 19, 16, 16, 728016)),
        ),
    ]
