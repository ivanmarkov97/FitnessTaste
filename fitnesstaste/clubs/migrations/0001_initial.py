# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-27 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=80)),
                ('club_adrees', models.CharField(max_length=160)),
                ('club_contact', models.CharField(max_length=80)),
                ('club_email', models.CharField(max_length=80)),
                ('club_description', models.TextField()),
            ],
        ),
    ]
