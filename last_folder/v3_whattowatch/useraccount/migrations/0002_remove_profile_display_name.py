# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='display_name',
        ),
    ]