# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 00:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Comments_app', '0004_remove_post_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
