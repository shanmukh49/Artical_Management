# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-05-30 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=50)),
                ('vote', models.IntegerField()),
            ],
        ),
    ]
