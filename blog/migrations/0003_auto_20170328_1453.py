# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='stars',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]