# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 09:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20180226_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(default=datetime.datetime(2018, 2, 26, 9, 21, 47, 84871)),
        ),
    ]
