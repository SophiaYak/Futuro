# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_auto_20171114_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='buying_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 14, 7, 29, 44, 242124)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='current_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 7, 29, 44, 242124)),
        ),
    ]
