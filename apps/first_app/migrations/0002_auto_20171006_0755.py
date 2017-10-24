# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 14:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='my_stock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.Stock'),
        ),
        migrations.AlterField(
            model_name='user',
            name='my_basket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.Basket'),
        ),
    ]
