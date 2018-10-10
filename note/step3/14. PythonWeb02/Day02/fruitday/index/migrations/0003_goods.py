# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-01 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20180301_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='商品名称')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='商品价格')),
                ('spec', models.CharField(max_length=30, verbose_name='商品规格')),
                ('picture', models.ImageField(upload_to='static/upload/goods', verbose_name='商品图片')),
                ('isActive', models.BooleanField(default=True, verbose_name='销售中')),
            ],
            options={
                'db_table': 'goods',
                'verbose_name_plural': '商品信息',
                'verbose_name': '商品信息',
            },
        ),
    ]