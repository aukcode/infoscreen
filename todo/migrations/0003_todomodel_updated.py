# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todomodel_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
