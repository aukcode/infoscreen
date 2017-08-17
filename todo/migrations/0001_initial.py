# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-10 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=255)),
                ('done', models.BooleanField(default=False)),
                ('priority', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
