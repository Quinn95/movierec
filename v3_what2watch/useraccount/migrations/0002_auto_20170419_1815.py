# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-19 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierec', '0001_initial'),
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='disliked_movies',
            field=models.ManyToManyField(related_name='disliked', to='movierec.Movie'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='liked_movies',
            field=models.ManyToManyField(related_name='liked', to='movierec.Movie'),
        ),
    ]