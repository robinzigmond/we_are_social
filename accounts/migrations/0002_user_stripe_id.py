# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_id',
            field=models.CharField(default='', max_length=40),
        ),
    ]
