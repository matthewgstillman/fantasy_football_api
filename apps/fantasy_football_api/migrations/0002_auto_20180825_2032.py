# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-25 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy_football_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='overall_standing',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='team',
            name='waiver_rank',
            field=models.IntegerField(),
        ),
    ]