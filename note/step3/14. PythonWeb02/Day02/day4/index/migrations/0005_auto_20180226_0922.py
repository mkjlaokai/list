# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-26 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20180226_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(),
        ),
    ]
