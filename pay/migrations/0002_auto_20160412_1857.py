# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-12 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fbId',
            field=models.CharField(default=-1, max_length=100),
            preserve_default=False,
        ),
    ]
