# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20160227_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='realname',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
