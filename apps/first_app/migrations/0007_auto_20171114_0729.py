# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-14 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_auto_20171114_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='PE',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='stock',
            name='adj_close',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stock',
            name='buying_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 14, 7, 29, 40, 226)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='change_pct',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stock',
            name='close_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stock',
            name='current_date',
            field=models.DateField(default=datetime.datetime(2017, 11, 14, 7, 29, 40, 226)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='high_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stock',
            name='last',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='stock',
            name='low_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stock',
            name='open_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stock',
            name='short_ratio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
