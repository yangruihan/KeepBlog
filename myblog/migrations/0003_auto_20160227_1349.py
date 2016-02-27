# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20160227_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('realname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=1)),
                ('birthday', models.DateField()),
                ('area', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.User'),
        ),
    ]
