# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-29 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170328_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='isdeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='ispublished',
            field=models.BooleanField(default=False),
        ),
    ]
