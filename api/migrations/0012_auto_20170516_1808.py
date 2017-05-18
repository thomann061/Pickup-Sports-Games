# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 22:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20170516_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameuser',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_info', to='api.Game'),
        ),
        migrations.AlterField(
            model_name='gameuser',
            name='organizerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizer_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='gameuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL),
        ),
    ]