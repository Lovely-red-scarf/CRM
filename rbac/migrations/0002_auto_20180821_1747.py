# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-21 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='icon',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='图标'),
        ),
        migrations.AddField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='是否可以做菜单'),
        ),
    ]