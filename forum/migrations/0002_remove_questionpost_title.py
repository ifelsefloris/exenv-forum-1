# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 13:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionpost',
            name='title',
        ),
    ]
