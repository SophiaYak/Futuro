# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 04:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0013_auto_20171109_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='buying_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 20, 17, 45, 509696)),
        ),
    ]
