# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-08 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20171229_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='board.Post'),
            preserve_default=False,
        ),
    ]