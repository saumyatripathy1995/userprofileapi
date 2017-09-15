# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('dob', models.DateField(max_length=50)),
                ('emails', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=400)),
            ],
        ),
    ]
