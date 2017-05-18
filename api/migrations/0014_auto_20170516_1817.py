# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0013_auto_20170516_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameuser',
            name='organizer',
        ),
        migrations.AddField(
            model_name='game',
            name='gameOrganizer',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='organizer_info', to=settings.AUTH_USER_MODEL),
        ),
    ]