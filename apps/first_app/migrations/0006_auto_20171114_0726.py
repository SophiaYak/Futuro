# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 15:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20171114_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='buying_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 14, 7, 26, 39, 479782)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='current_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 7, 26, 39, 479782)),
        ),
    ]
