# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-17 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField(default=-1)),
                ('name', models.CharField(default='SOME STRING', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField(unique=True)),
                ('themoviedb', models.IntegerField(null=True)),
                ('imdb', models.CharField(max_length=200, null=True)),
                ('rating', models.CharField(max_length=7)),
                ('rottentomatoes', models.IntegerField(null=True)),
                ('wikipedia_id', models.IntegerField(null=True)),
                ('metacritic', models.CharField(max_length=200, null=True)),
                ('common_sense_media', models.CharField(max_length=200, null=True)),
                ('poster', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=30, null=True)),
                ('date', models.IntegerField(null=True)),
                ('language', models.CharField(max_length=2, null=True)),
                ('netflix', models.CharField(max_length=200, null=True)),
                ('amazon', models.CharField(max_length=200, null=True)),
                ('hulu', models.CharField(max_length=200, null=True)),
                ('trailer', models.CharField(max_length=200, null=True)),
                ('genre', models.ManyToManyField(to='movierec.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.IntegerField(default=-1)),
                ('name', models.CharField(default='SOME STRING', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='people',
            field=models.ManyToManyField(to='movierec.Person'),
        ),
    ]