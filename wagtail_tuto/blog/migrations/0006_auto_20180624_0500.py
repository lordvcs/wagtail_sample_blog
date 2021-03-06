# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-24 05:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import wagtailmd.utils


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_postpage_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpage',
            name='body',
            field=wagtailmd.utils.MarkDownField(),
        ),
        migrations.AlterField(
            model_name='postpage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='Post date'),
        ),
    ]
