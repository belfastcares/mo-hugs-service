# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
