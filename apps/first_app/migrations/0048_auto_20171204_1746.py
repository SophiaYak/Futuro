# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 01:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0047_auto_20171204_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='buying_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 17, 46, 25, 74869)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='current_date',
            field=models.DateField(default=datetime.datetime(2017, 12, 4, 17, 46, 25, 74869)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='past_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 4, 17, 46, 25, 74869)),
        ),
    ]
