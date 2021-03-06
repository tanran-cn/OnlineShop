# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-26 22:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20180226_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='order_sn',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='订单号'),
        ),
        migrations.AlterField(
            model_name='orderinfo',
            name='pay_status',
            field=models.CharField(choices=[('success', '成功'), ('cancel', '取消'), ('paying', '待支付')], default='paying', max_length=10, verbose_name='订单状态'),
        ),
    ]
