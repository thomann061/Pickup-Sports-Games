# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20170516_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameuser',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Game'),
        ),
    ]
