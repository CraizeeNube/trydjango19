# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-10 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
