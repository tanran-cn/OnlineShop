# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20171222_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodscategorybrand',
            name='cagetory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
    ]
