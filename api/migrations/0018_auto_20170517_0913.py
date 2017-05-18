# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-17 13:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_game_gameorganizerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='gameOrganizerId',
        ),
        migrations.AlterField(
            model_name='game',
            name='gameOrganizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]