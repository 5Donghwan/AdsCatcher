# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-11 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170611_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='state',
            field=models.CharField(default='', max_length=10),
        ),
    ]
