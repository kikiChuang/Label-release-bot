# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0023_remove_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
    ]
